from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название', max_length=80)
    content = models.TextField(blank=True, null=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото")
    data = models.DateField('Дата публикации')
    cat_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
  
    