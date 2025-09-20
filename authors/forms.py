from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'id': 'required'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'id': 'required'})
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'id': 'required', 'placeholder': 'e.g. +1234567890'})
    )
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'id': 'required'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'birthdate', 'password1', 'password2']



class UserUpdateForm(UserChangeForm):
    password = None  # Hide the password field (optional)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    