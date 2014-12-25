from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$',home, name='home'),
    url(r'^ping/$',ping, name='ping'),
    url(r'^schema/(?P<version>.+)/$',schema, name='schema'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
