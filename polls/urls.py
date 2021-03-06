from django.conf.urls import url
from django.utils import timezone
from django.views.generic import ListView, DetailView

from polls import views
from polls.models import Poll

#
# urlpatterns = patterns('',
#                        url(r'^$', views.index, name='index'),
#                        url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#                        url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#                        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'))


urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Poll.objects.filter(pub_date__lt=timezone.now())
                     .order_by('-pub_date')[:5],
        context_object_name='latest_poll_list',
        template_name='polls/index.html'
    ), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
        model=Poll,
        template_name='polls/detail.html'
    ), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', DetailView.as_view(
        model=Poll,
        template_name='polls/results.html'), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')]
