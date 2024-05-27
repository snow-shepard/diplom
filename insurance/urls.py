from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('osago/', osago, name='osago'),
    path('isa/', isa, name='isa'),
    path('news/', news_list, name='news_list'),
]