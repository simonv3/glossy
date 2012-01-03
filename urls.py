from django.conf.urls.defaults import patterns, include, url
from glossy_app.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    (r'^import/austronesian/$', import_austronesian),
    (r'^$', splash),
    (r'^home', direct_to_template, {'template': 'vanlittjan.html'}),
     
    # Examples:
    # url(r'^$', 'glossy.views.home', name='home'),
    # url(r'^glossy/', include('glossy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^language/(?P<languageid>\w+)/(?P<order>\w+)/$',language),
    url(r'^language/(?P<languageid>\w+)/$',language),
    url(r'^word/(?P<wordid>\w+)/$', word),
    # all my other url mappings
    (r'^accounts/profile/$', profile),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'glossy/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    {'next_page':'/'}),
    (r'^api/', include('glossy_app.api.urls')),
   
    
)

