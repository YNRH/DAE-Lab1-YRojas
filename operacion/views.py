from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Desde la vista de operacion!")

def suma(request, num1, num2):
    sum = num1+num2
    return HttpResponse("<h1>La suma de %s + %s = %s <h1/>" % (num1, num2, sum))

def resta(request, num1, num2):
    res = num1-num2
    return HttpResponse("<h1>La resta de %s - %s = %s <h1/>" % (num1, num2, res))

def multiplicacion(request, num1, num2):
    multi = num1*num2
    return HttpResponse("<h1>La multiplicacion de %s * %s = %s <h1/>" % (num1, num2, multi))
