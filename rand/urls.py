from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randint/', views.randint, name='randint'),
    path('lottery/', views.lottery, name='lottery'),
    path('group/', views.group, name='group'),
    path('dice_throw/', views.dice_throw, name='dice_throw'),
    path('group_randomizer/', views.group_randomizer, name='group_randomizer'),
    path('elements_draw/', views.elements_draw, name='elements_draw'),
    path('coin/', views.coin, name='coin'),
]
