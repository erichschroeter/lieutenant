from django.conf.urls import patterns, url

from django.views.generic.edit import CreateView

from tags import views

from taggit.managers import TaggableManager

urlpatterns = patterns('',
    url(r'^$', views.TagList.as_view(), name='index'),
    url(r'^update/(?P<slug>[^/]+)/$', views.TagUpdate.as_view(success_url="/tags/"), name='update'),
    url(r'^delete/(?P<slug>[^/]+)/$', views.TagDelete.as_view(), name='delete'),
    url(r'^(?P<slug>[^/]+)/$', views.TagRead.as_view(), name='detail'),
)
