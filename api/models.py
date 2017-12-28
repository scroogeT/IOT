# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
