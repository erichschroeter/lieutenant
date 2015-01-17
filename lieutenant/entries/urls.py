from django.conf.urls import patterns, url

from entries import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
