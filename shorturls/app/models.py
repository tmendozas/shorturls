from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Link(models.Model):
    creation_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    short_url = models.CharField(max_length=10,db_index=True,unique=True)
    real_url = models.TextField(db_index=True)
    
    class Meta:
        db_table = 'link'

    def __str__(self):
        return self.name