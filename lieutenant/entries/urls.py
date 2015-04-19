from django.conf.urls import patterns, url

from django.views.generic.edit import CreateView

from entries import views
from entries.views import EntryCreate, EntryRead, EntryUpdate, EntryDelete
from entries.models import Entry

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', EntryRead.as_view(), name='detail'),
    url(r'^create/$', EntryCreate.as_view(success_url="/entries/"), name='create'),
    url(r'^update/(?P<pk>\d+)/$', EntryUpdate.as_view(success_url="/entries/"), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', EntryDelete.as_view(), name='delete'),
)
