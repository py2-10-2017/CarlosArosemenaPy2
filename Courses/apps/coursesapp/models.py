from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}

        if len(postData['course_name']) < 5 or len(postData['course_description']) < 15:
            errors['length'] = "Course name must be 5 characters and the description at least 15"

        return errors

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class description(models.Model):
    description = models.TextField()
    course = models.OneToOneField(course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
