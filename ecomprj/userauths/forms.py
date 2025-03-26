from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is mandatory
    class Meta:
        model=User
        fields=['username','email']