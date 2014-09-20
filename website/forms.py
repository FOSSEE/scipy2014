from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

from website.models import Proposal

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username is None or password is  None:
            raise forms.ValidationError("Invalid username or password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password")
        if not user.is_active:
            raise forms.ValidationError("User is blocked")
        cleaned_data['user'] = user
        return cleaned_data

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '')
        if not first_name:
            raise forms.ValidationError("First name cannot be blank.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '')
        if not last_name:
            raise forms.ValidationError("Last name cannot be blank.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        validate_email(email)

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username) < 6:
            raise forms.ValidationError("Required a minimum 6 character username.")
        return username

class ProposalForm(forms.ModelForm):
    link = forms.CharField(required=False)
    class Meta:
        model = Proposal
        exclude = ('user')

    def clean_attachment(self):
        cleaned_data = self.cleaned_data
        attachment = cleaned_data.get('attachment', None)
        if attachment:
            if not attachment.name.endswith('.pdf'):
                raise forms.ValidationError('Only [.pdf] files are allowed')
            elif attachment.size > (5*1024*1024):
                raise forms.ValidationError('File size exceeds 5MB')
        return attachment
