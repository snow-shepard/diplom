from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
  
    def __str__(self):
        return self.title