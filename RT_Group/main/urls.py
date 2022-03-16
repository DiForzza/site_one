from django.urls import path
from main import views
from django.urls import include

app_name = "main"

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('authorization', views.authorization, name="authorization"),
    path('accounts/', include('django.contrib.auth.urls')),
]