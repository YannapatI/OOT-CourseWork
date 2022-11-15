from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from django.template import loader
from django.urls import reverse

def index(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def colorpencil(request):
    template = loader.get_template('colorpencil.html')
    return HttpResponse(template.render())
    
def eraser(request):
    template = loader.get_template('eraser.html')
    return HttpResponse(template.render())

def notebook(request):
    template = loader.get_template('notebook.html')
    return HttpResponse(template.render())

def pen(request):
    template = loader.get_template('pen.html')
    return HttpResponse(template.render())

def pencil(request):
    template = loader.get_template('pencil.html')
    return HttpResponse(template.render())
