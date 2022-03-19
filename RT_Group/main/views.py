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
    # if request.method == 'POST':
    #     form = UserLoginForm(request.POST or None)
    #     if form.is_valid():
    #         username = User.objects.get(email=form.cleaned_data['email'])
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             if user.is_active:
    #                 auth_login(request, user)
    #                 return HttpResponseRedirect(request.GET.get('next',
    #                                                             settings.LOGIN_REDIRECT_URL))
    #         else:
    #             error = 'Invalid username or password.'
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
    return render(request, 'main/add_news.html', context)


def testpage(request):
    return render(request, 'main/testpage.html', {'response': weather()})
