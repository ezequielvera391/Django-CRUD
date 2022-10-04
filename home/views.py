from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index')
def hola_mundo(request, name='hernan'):
    return HttpResponse(f'Hola {name}' )