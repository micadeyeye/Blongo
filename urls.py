from django.conf.urls.defaults import patterns, include, url
from blongo.blogapp.views import *
from blongo.registration import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blongo.views.home', name='home'),
    # url(r'^blongo/', include('blongo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url mapping added by micadeyeye
    url(r'^$', 'blongo.blogapp.views.index'),
    url(r'^admin/publications/$', 'blongo.blogapp.views.publications'),
    url(r'^admin/update/$', 'blongo.blogapp.views.update'),
    url(r'^admin/sections/$', 'blongo.blogapp.views.sections'),
    url(r'^admin/profile/$', 'blongo.blogapp.views.profile'),
    url(r'^admin/delete/$', 'blongo.blogapp.views.delete'),
    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'blongo.blogapp.views.logout_page'),
    url(r'^admin/$', 'blongo.blogapp.views.admin_page'),
    #next line added by micadeyeye to support the django-registration-me app
    url(r'^accounts/', include('blongo.registration.urls')),

)
