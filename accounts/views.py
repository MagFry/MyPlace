from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import RegistrationForm, UserEditForm, UserProfileEditForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('chat:list')
        else:
            messages.error(request, 'Wrong credentials. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })


@login_required
def registration_done(request):
    return render(request, 'accounts/registration_done.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = UserProfile.objects.create(user=new_user)
            return render(request,'accounts/registration_done.html', {'user':new_user})
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    form = RegistrationForm(request.GET)
    return render(request, 'accounts/user_profile.html',{ 'form': form })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm (instance=request.user, data=request.POST)
        user_profile_form = UserProfileEditForm (instance=request.user.userprofile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Provided data is not sufficient or it has wrong format, please try again. Remember to fill all data excluding photo.')
    else:
        user_form = UserEditForm(instance=request.user)
        user_profile_form = UserProfileEditForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit.html', {'user_form': user_form, 'user_profile_form': user_profile_form})


@login_required
def logout_view(request):
        logout(request)
        return render(request, 'accounts/logout.html')

