from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    """Sign up a new user"""
    # Validate form data
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)

            return redirect('article_list')
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form":form})

def login_view(request):
    """Login a user"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect users to the create article page coming from there and logged out
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('article_list')
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    """Log out users"""
    if request.method == "POST":
        logout(request)

        return redirect("article_list")

