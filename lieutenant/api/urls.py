from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^entries/$', views.EntryList.as_view()),
    url(r'^entries/(?P<pk>\d+)/$', views.EntryRead.as_view()),
)
