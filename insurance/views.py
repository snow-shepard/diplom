from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    return HttpResponse('СТ 1')

def categories(request, cat):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f'<h1>Ст по ктг</h1><p>{cat}</p>')

def archive(request, year):
    if int(year) > 2020:
        a = redirect('home', permanent=True)
        return a
    return HttpResponse(f'<h1>Архиве</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ст нот фанде</h1>')