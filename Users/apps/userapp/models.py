from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.db import models

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        try:
            validate_email(postData["email_address"])
        except ValidationError:
            errors['email'] = "invalid email"



        checkEmail = users.objects.filter(email_address=postData["email_address"])

        if checkEmail:
            errors['email']= "email already exists"


        if len(postData['first_name']) < 2:
            errors["first_name"] = "names should be more than 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "names should be more than 2 characters"

        return errors



# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
