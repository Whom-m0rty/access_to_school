"""acess_to_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('api/<str:slug>/', PostView.as_view()),
    path('view/<str:slug>/', views.view),
    path('api/create/<str:first_name>/<str:surname>/<str:patronymic>/<str:email>/', views.api_create, name='create_api'),
    path('api/commit/<str:slug>/', views.api_commit),
    path('', views.index),
    path('missing/', views.missing, name='missing'),
    path('create/', Create.as_view(), name='create')
]
