from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^entries/$', views.EntryList.as_view()),
    url(r'^entries/(?P<year>(\d\d\d\d))/$', views.EntryList.as_view(), name='list-year'),
    url(r'^entries/(?P<year>(\d\d\d\d))/(?P<month>(\d\d))/$', views.EntryList.as_view(), name='list-month'),
    url(r'^entries/(?P<year>(\d\d\d\d))/(?P<month>(\d\d))/(?P<day>(\d\d))/$', views.EntryList.as_view(), name='list-day'),
    url(r'^entries/(?P<slug>[^/]+)/$', views.EntryDetail.as_view()),
    url(r'^tags/$', views.TagsList.as_view()),
)

