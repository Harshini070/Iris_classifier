# predictor/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Home page mapped to root URL
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
]
