from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'item_detail', None, {'object_id': self.id}

    class Meta:
        ordering = ['name']


class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'phone_detail', None, {'object_id': self.id}

    class Meta:
        ordering = ['title']
