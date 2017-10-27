from __future__ import unicode_literals
from ..log_reg.models import *
from django.db import models


class messagepost(models.Model):
    message = models.TextField()
    poster = models.ForeignKey(users, related_name='poster')
    user_id = models.ForeignKey(users, related_name='messagespost')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class commentpost(models.Model):

    comment = models.TextField()
    user_id = models.ForeignKey(users, related_name='commentpost')
    message_id = models.ForeignKey(messagepost, related_name="message_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
