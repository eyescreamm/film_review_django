from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(forms.Form):
    email = forms.EmailField(label="email")
    name = forms.CharField(max_length=20, label="username")
    password = forms.CharField(max_length=20, label="password")

class LoginForm(forms.Form):
    name = forms.CharField(max_length=20, label="username")
    password = forms.CharField(max_length=20, label="password")

class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=5, label="rating")
    comment = forms.CharField(required=False)

class SortForm(forms.Form):
    choice = forms.fields.ChoiceField(
        choices = (
            ('name', 'name'),
            ('rating', 'rating'),
            ('review', 'review'),
        ),
    )