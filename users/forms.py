from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re


class UserRegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.findall(r'[0-9]+', username):
            raise forms.ValidationError('the username must be contains numbers😦')
        try:
            user = User.objects.get(username=username)
            if user:
                raise forms.ValidationError(f'Username "{username}" is already in use.😐')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            exist_email = User.objects.get(email=email)
            if exist_email:
                raise forms.ValidationError(f'this email "{email}" is already in use.😐')
        except User.DoesNotExist:
            return email


class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
