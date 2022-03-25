from django.urls import path
from main import views
from django.urls import include

app_name = "main"

urlpatterns = [
    path('', views.us_context, name="home"),
    path('about', views.us_context, name="about"),
    path('authorization', views.us_context, name="authorization"),
    path('add_news', views.add_news, name="add_news"),
    path('testpage', views.us_context, name="testpage"),
    path('accounts/', include('django.contrib.auth.urls')),
]