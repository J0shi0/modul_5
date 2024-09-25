from django import forms
from .models import UserModel, Note
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
