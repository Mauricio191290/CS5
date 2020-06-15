from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.models import User
from django.conf.urls import include 
from django.conf.urls import url
from Login.views import CustomAuthToken



urlpatterns = [
    re_path(r'^', CustomAuthToken.as_view()),
]