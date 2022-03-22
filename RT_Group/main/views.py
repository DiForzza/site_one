from django.shortcuts import render, redirect
import requests
from .models import Task
from .forms import TaskForm
from django.urls import resolve
import datetime


def weather():
    url = 'http://wttr.in/Ekaterinburg?0T'
    response = requests.get(url, params={'format': 2, 'M': ''})
    return response.text


def us_context(request):
    error = ''
    form = ''
    tasks = Task.objects.order_by('-id')[:3]
    current_url = resolve(request.path_info).url_name
    time = datetime.datetime.now()
    if request.path_info == '/':
        title = 'Главная страница'
    elif request.path_info == '/about':
        title = 'О нас'
    else:
        title = ''
    return {
        'response': weather(),
        'tasks': tasks,
        'current_url': current_url,
        'time': time,
        'title': title,
        'error': error,
        'form': form,
    }


def index(request):
    return render(request, 'main/main.html', us_context(request))


def about(request):
    return render(request, 'main/about.html', us_context(request))


def authorization(request):
    return render(request, 'registration/login.html', us_context(request))


def testpage(request):
    return render(request, 'main/testpage.html', us_context(request))


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    title = 'Добавить новость'
    context = {
        'form': form,
        'error': error,
        'title': title
    }
    if request.user.is_authenticated:
        # print('user ' + request.user.get_full_name())  # get_short_name() || request.user.first_name ||
        # request.user.last_name
        return render(request, 'main/add_news.html', context)
    else:
        return redirect('main:home')
