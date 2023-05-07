from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'password1', 'password2')


