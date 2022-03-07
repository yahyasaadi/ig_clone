from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# The forms
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    fullname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    fullname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']