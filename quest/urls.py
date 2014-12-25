from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from django.contrib import admin
from django_markdown import flatpages

admin.autodiscover()
flatpages.register()

urlpatterns = patterns('',
    url('^$',home, name='home'),
    url(r'^ping/$',ping, name='ping'),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),

)
urlpatterns += staticfiles_urlpatterns()
# urlpatterns = patterns('',
#     (r'^pages/', include('django.contrib.flatpages.urls')),
# )

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^ping/details/$', 'flatpage', {'url': '/ping/details/'}, name='pingdetails'),
    url(r'^schema/details/$', 'flatpage', {'url': '/schema/details/'}, name='schemadetails'),
    url(r'^schema/v1.1/$', 'flatpage', {'url': '/schema/v1.1/'}, name='schemav1.1'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
