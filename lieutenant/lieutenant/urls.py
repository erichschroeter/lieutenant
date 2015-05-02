from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lieutenant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^entries/', include('entries.urls', namespace="entries")),
)
