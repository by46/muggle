from django.conf.urls import url

from .views import BookDetails, BookIndex, add_book, thanks

__author__ = 'benjamin.c.yan'

urlpatterns = [url(r'^$', BookIndex.as_view(), name='index'),
               url(r'^(?P<pk>\d+)/$', BookDetails.as_view(), name='book'),
               url(r'^add$', add_book, name='newbook'),
               url(r'^thanks$', thanks, name='thanks'),
               ]
