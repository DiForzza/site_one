from django.shortcuts import render
import requests
from .models import Task

def weather():
    url = 'http://wttr.in/Ekaterinburg?0T'
    response = requests.get(url, params={'format': 2, 'M': ''})
    return response.text


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/main.html', {'response': weather(), 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html', {'response': weather()})


def authorization(request):
    return render(request, 'main/authorization.html', {'response': weather()})
