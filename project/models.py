from django.db import models

# Create your models here.

from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    title_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.name)



