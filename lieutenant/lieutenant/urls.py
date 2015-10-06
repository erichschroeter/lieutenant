from django.conf.urls import patterns, include, url
from django.contrib import admin

from lieutenant.views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lieutenant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^entries/', include('entries.urls', namespace="entries")),
    url(r'^tags/', include('tags.urls', namespace="tags")),
)
