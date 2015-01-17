from django.conf.urls import patterns, include, url
from django.contrib import admin

from entries import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lieutenant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^entries/', include('entries.urls', namespace="entries")),
)
