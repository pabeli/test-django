from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from todolist.views import index

urlpatterns = [
    path('', index, name='todolist'),
]
