# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class device(models.Model):
    owner = models.CharField(max_length=20, blank=True, unique=True)
    make = models.CharField(max_length=20, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    #light controls
    light1isON = models.BooleanField(default=False)
    light2isON = models.BooleanField(default=False)
    light3isON = models.BooleanField(default=False)
    #others
    stove1State = models.IntegerField(default=0)
    fan1State = models.IntegerField(default=0)
    geyser1State = models.IntegerField(default=0)
    homeTemp = models.FloatField(default=0)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} : {}".format(self.make, self.owner)

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)