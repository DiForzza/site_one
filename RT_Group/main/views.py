from django.shortcuts import render
import requests


def index(request):
    url = 'http://wttr.in/Ekaterinburg?0T'
    response = requests.get(url)
    return render(request, 'main/main.html', {'response': response.text})


def about(request):
    return render(request, 'main/about.html')
