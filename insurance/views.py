from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *


def index(request):
    posts = News.objects.all()
    return render(request, 'insurance/index.html', {'posts':posts, 'title': 'ГС'})

def osago(request):
    return render(request, 'insurance/osago.html', {'title': 'ОСАГО'})

def isa(request):
    return render(request, 'insurance/isa.html', {'title': 'ИС'})

def categories(request, cat):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f'<h1>Ст по ктг</h1><p>{cat}</p>')

def archive(request, year):
    if int(year) > 2020:
        a = redirect('/', permanent=True)
        return a
    return HttpResponse(f'<h1>Архиве</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ст нот фанде</h1>')