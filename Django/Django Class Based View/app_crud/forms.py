from django import forms
from app_crud import models
from django.core import validators


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class' : 'form-control'}),
        }