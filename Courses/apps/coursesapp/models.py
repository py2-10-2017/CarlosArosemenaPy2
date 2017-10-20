from __future__ import unicode_literals

from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class description(models.Model):
    description = models.TextField()
    course = models.OneToOneField(course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
