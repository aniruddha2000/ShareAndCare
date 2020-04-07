from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *


def home_view(request):
    return render(request, 'account/home.html')

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('homepage:home', user.username)
    return render(request, 'account/login.html', {'form': form})

def signup_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('homepage:home', user.username)

    args = {
        'form': form,
    }
    return render(request, "account/signup.html", args)

@login_required(login_url='account:login')
def profile_view(request):
    user_form = EditProfileForm(request.POST or None, instance=request.user)
    user_profile_form = EditUserProfileForm(request.POST or None, instance=request.user.userprofile)
    args = {
        'username': request.user,
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }
    return render(request, "account/profile.html", args)

@login_required(login_url='account:login')
def edit_profile_view(request):
    user_form = EditProfileForm(request.POST or None, instance=request.user)
    user_profile_form = EditUserProfileForm(request.POST or None, instance=request.user.userprofile)
    if user_form.is_valid() and user_profile_form.is_valid():
        form = user_form.save()
        custom_form = user_profile_form.save(False)
        custom_form.user = form
        custom_form.save()
        return redirect('account:profile')

@login_required(login_url='account:login')
def logout_view(request):
    logout(request)
    return redirect('account:login')
