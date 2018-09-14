from django.shortcuts import render, redirect
from accounts.forms import (RegistrationForm,
EditProfileForm)

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash # to make sure user is logged in even after password change

from django.contrib.auth.decorators import login_required # to make sure the views only work if the user is logged in, its just a decorator

# Create your views here.
# function based views


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else: # First time is GET, i.e Asking for the blank form
        form = RegistrationForm()

        args = {'form' : form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    context = {'user': request.user}
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        context = {'form' : form}
        return render(request, 'accounts/edit_profile.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)


        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            print('here')
            return redirect('/account/change-password') # VIDEO 20 - 22 MAX GOODRIDGE

    else:
        form = PasswordChangeForm(user=request.user)

        context = {'form': form}

        return render(request, 'accounts/change_password.html', context)
