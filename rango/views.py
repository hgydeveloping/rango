from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import getpass

def index(request):
    context_dict = {'boldmessage': "Hello World!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'myname': getpass.getuser()}
    return render(request, 'rango/about.html', context=context_dict)

def test1(request):
    context_dict = {'myvar1': "Teszt valtozo"}
    return render(request, 'rango/test1.html', context=context_dict)
