from django.shortcuts import render, redirect
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
    return render(request, 'main/main.html', {
        'response': weather(),
        'tasks': tasks,
        'current_url': setup(request)
    })


def about(request):
    return render(request, 'main/about.html', {'response': weather()})


def authorization(request):
    error = ''
    context = {
        'response': weather(),
        'error': error
    }
    return render(request, 'registration/login.html', context)


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
    context = {
        'form': form,
        'error': error,
        'response': weather(),
    }
    if request.user.is_authenticated:
        print('user ' + request.user.get_full_name())  # get_short_name() || request.user.first_name ||
        # request.user.last_name
        return render(request, 'main/add_news.html', context)
    else:
        return redirect('main:home')


def testpage(request):
    return render(request, 'main/testpage.html', {'response': weather()})
