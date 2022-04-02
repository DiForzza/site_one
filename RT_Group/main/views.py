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
    context_list = {}
    tasks = Task.objects.order_by('-id')[:3]
    current_url = resolve(request.path_info).url_name
    time = datetime.datetime.now()
    context_list['response'] = weather()
    context_list['current_url'] = current_url
    context_list['time'] = time
    print(request.path_info)
    if request.path_info == '/':
        context_list['title'] = 'Главная страница'
        context_list['tasks'] = tasks
        return render(request, 'main/main.html', context_list)
    elif request.path_info == '/about':
        context_list['title'] = 'О нас'
        return render(request, 'main/about.html', context_list)
    # elif request.path_info == '/testpage':
    #     context_list['text'] = 'AndreyEX'
    #     context_list['title'] = 'Тестовая страница'
    #    return render(request, 'main/testpage.html', context_list)
    else:
        context_list['title'] = ''
    return context_list


def testpage(request):
    print('tessss')
    return render(request, 'main/testpage.html')


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
        'title': title,
        'response': weather()
    }
    if request.user.is_authenticated:
        # print('user ' + request.user.get_full_name())  # get_short_name() || request.user.first_name ||
        # request.user.last_name
        return render(request, 'main/add_news.html', context)
    else:
        return redirect('main:home')
