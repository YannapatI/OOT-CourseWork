from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('colorpencil/', views.colorpencil, name='colorpencil'),
    path('eraser/', views.eraser, name='eraser'),
    path('notebook/', views.notebook, name='notebook'),
    path('pen/', views.pen, name='pen'),
    path('pencil/', views.pencil, name='pencil'),
]
