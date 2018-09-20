from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Define meta data that relates to the data in this class
    class Meta:
        model = User
        # These are names of fields that must be displayed
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    # include and exclude forms using meta
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        # MUST INCLUDE PASSWORD FIELD
        # there is also exclude()
