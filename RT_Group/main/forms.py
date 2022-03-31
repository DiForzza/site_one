from .models import Task, SendEmail
from django.forms import ModelForm, TextInput, Textarea


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


class SendEmailForm(ModelForm):
    class Meta:
        model = SendEmail
        fields = ['email', 'text']
        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }