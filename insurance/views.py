from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import *


def index(request):
    now = timezone.now()
    recent_time_threshold = now - timedelta(days=30)
    news_items = News.objects.filter(is_published=True, time_create__gte=recent_time_threshold).order_by('-time_create')[:4]
    return render(request, 'insurance/index.html', {'news_items': news_items, 'title': 'ГС'})

def osago(request):
    faq_items = FAQ.objects.filter(is_published=True)[:4]
    return render(request, 'insurance/osago.html', {'faq_items': faq_items, 'title': 'ОСАГО'})

def isa(request):
    faq_items = FAQ.objects.filter(is_published=True)[:4]
    return render(request, 'insurance/isa.html', {'faq_items': faq_items,'title': 'ИС'})

def news_list(request):
    news_items = News.objects.filter(is_published=True).order_by('-time_create')[:4]
    return render(request, 'insurance/news.html', {'news_items': news_items, 'title': 'НОВОСТИ'})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'insurance/post.html', {'news': news})

def faq(request):
    faq_items = FAQ.objects.filter(is_published=True)
    return render(request, 'insurance/faq.html', {'faq_items': faq_items, 'title': 'ВОПРОСЫ'})

def archive(request, year):
    if int(year) > 2020:
        a = redirect('/', permanent=True)
        return a
    return HttpResponse(f'<h1>Архиве</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ст нот фанде</h1>')

