from django.conf.urls import url

from .views import BookDetails, BookIndex

__author__ = 'benjamin.c.yan'

urlpatterns = [url(r'^$', BookIndex.as_view(), name='index'),
               url(r'^(?P<pk>\d+)/$', BookDetails.as_view(), name='book'),
               ]
