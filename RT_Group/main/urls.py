from django.urls import path
from main import views
from django.urls import include
from main.views import TestAPIView


app_name = "main"

urlpatterns = [
    path('', views.us_context, name="home"),
    path('about', views.us_context, name="about"),
    path('authorization', views.us_context, name="authorization"),
    path('add_news', views.add_news, name="add_news"),
    path('testpage', views.testpage, name="testpage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/testlist', TestAPIView.as_view())
]