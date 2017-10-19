from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.db import models

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        try:
            validate_email(postData['email_address'])
        except ValidationError:
            errors['email'] = "Invalid email"

        checkIfEmailInDB = restuser.objects.filter(email_address=postData["email_address"])

        if checkIfEmailInDB:
            errors['email'] = "email already exists"

        if len(postData['first_name'])< 2 or len(postData['last_name'])< 2:
            errors['name']= "first and last name must be greater than 2 characters"

        return errors

    def update_user_validator(self, postData):
        errors = {}
        try:
            validate_email(postData['email_address'])
        except ValidationError:
            errors['email'] = "Invalid email"

        # checkIfEmailInDB = restuser.objects.filter(email_address=postData["email_address"])
        #
        # if checkIfEmailInDB:
        #     errors['email'] = "email already exists"

        if len(postData['first_name'])< 2 or len(postData['last_name'])< 2:
            errors['name']= "first and last name must be greater than 2 characters"

        return errors
# Create your models here.
class restuser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
