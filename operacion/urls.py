from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ex: localhost:8000/app/sumar/4/6/
    path('sumar/<int:num1>/<int:num2>', views.suma, name='sumar'),
    # ex: localhost:8000/app/restar/4/6/
    path('restar/<int:num1>/<int:num2>', views.resta, name='restar'),
    # ex: localhost:8000/app/multiplicar/4/6/
    path('multiplicar/<int:num1>/<int:num2>', views.multiplicacion, name='multiplicar'),
]