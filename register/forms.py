from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # if we created another field here like "gender" it should be 
    # writen in the Meta class "field" list below

    # it needs to be named meta, and it needs to save into the users db
    class Meta:
        model = User
        # this will specify in which order it will show up
        fields = ["username", "email", "password1", "password2"]
