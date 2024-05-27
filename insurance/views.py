from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.utils import timezone
from datetime import timedelta

from .models import *


def index(request):
    now = timezone.now()
    recent_time_threshold = now - timedelta(days=30)
    news_items = News.objects.filter(is_published=True, time_create__gte=recent_time_threshold).order_by('-time_create')[:4]
    return render(request, 'insurance/index.html', {'news_items': news_items, 'title': 'ГС'})

def osago(request):
    return render(request, 'insurance/osago.html', {'title': 'ОСАГО'})

def isa(request):
    return render(request, 'insurance/isa.html', {'title': 'ИС'})

def news_list(request):
    news_items = News.objects.filter(is_published=True).order_by('-time_create')[:4]
    return render(request, 'insurance/news.html', {'news_items': news_items, 'title': 'НОВОСТИ'})

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