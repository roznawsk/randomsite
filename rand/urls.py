from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randint/', views.randint, name='randint'),
    path('lottery/', views.lottery, name='lottery'),
    path('group/', views.group, name='group'),
]