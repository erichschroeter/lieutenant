from django.conf.urls import patterns, url

from django.views.generic.edit import CreateView

from entries import views
from entries.models import Entry

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', CreateView.as_view(model=Entry, success_url="/entries/"), name='create'),
)
