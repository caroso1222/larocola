from django.conf.urls import patterns, url

from songs import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'larocola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<year>\w+)/$',views.videos, name = 'videos'),
    url(r'^$', views.index, name = 'index'),
)