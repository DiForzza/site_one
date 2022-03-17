from django.shortcuts import render
import requests
from .models import Task
from .forms import TaskForm
from django.urls import resolve


def setup(request):
    current_url = resolve(request.path_info).url_name
    return current_url


def weather():
    url = 'http://wttr.in/Ekaterinburg?0T'
    response = requests.get(url, params={'format': 2, 'M': ''})
    return response.text


def index(request):
    tasks = Task.objects.order_by('-id')[:2]
    return render(request, 'main/main.html', {'response': weather(), 'tasks': tasks, 'current_url': setup(request)})


def about(request):
    return render(request, 'main/about.html', {'response': weather()})


def authorization(request):
    return render(request, 'registration/login.html', {'response': weather()})


def add_news(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_news.html', {'response': weather()}, context)