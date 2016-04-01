from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView

__author__ = 'benjamin.c.yan'

patterns = patterns('',
                    url(r'^book/(?P<object_id>\d+)/$', detail))


