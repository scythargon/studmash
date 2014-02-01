from django.conf.urls import patterns, include, url
from main import views as main_views
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    url(r'^$', main_views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
