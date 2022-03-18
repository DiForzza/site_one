from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите новость'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 100)