from django.conf.urls.defaults import patterns, include, url
from glossy_app.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', main),
    (r'^glossy/$', direct_to_template, {'template': 'glossy_index.html'}),
    (r'^glossy/home', direct_to_template, {'template': 'vanlittjan.html'}),
     
    # Examples:
    # url(r'^$', 'glossy.views.home', name='home'),
    # url(r'^glossy/', include('glossy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    
    )
