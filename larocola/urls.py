from django.conf.urls import patterns, include, url
from django.contrib import admin
from songs import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'larocola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ops/', include('ops.urls')),
	url(r'^year/', include('songs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )