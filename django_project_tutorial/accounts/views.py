from django.shortcuts import render, redirect
from accounts.forms import (RegistrationForm,
EditProfileForm,
PasswordChangeForm)

from django.contrib.auth.models import User

# Create your views here.
# function based views
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = "Moturu Vineeth"
    context = {'name' : name, 'numbers' : numbers}
    return render(request, 'accounts\\home.html', context)


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
