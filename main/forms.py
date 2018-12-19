from django import forms

from .models import User

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class LoginForm(forms.Form):

    username = forms.CharField(label='username', max_length=128, min_length=3)
    password = forms.CharField(label='password', max_length=128, min_length=3)

    class Meta:
        fields = ('username', 'password')