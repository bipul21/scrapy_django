from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Questions(models.Model):
    title = models.CharField(max_length=512)
    identifier =models.CharField(max_length=256)
    url = models.CharField(max_length=1024)

    def __unicode__(self):
        return "{} - {}".format(self.identifier,self.title)