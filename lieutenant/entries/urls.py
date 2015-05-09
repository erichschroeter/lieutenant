from django.conf.urls import patterns, url

from django.views.generic.edit import CreateView

from entries import views
from entries.views import EntryList, EntryCreate, EntryRead, EntryUpdate, EntryDelete
from entries.models import Entry

urlpatterns = patterns('',
    url(r'^$', EntryList.as_view(), name='index'),
    url(r'^create/$', EntryCreate.as_view(success_url="/entries/"), name='create'),
    url(r'^update/(?P<slug>[^/]+)/$', EntryUpdate.as_view(success_url="/entries/"), name='update'),
    url(r'^delete/(?P<slug>[^/]+)/$', EntryDelete.as_view(), name='delete'),
    url(r'^(?P<slug>[^/]+)/$', EntryRead.as_view(), name='detail'),
)
