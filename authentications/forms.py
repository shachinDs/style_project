from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class ModifiedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'e.g. Harry', 'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'e.g. Potter', 'class' : 'form-control'}))


    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'create a password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'confirm your password'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        widgets = {
            'username' : TextInput ( attrs={'placeholder':'e.g. harrypotter', 'class' : 'form-control'}),
        }

