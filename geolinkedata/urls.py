from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),

    #geolinkedata rest api
    url(r'^', include('api.urls')),
    #geolinkedata rest api swagger
    url(r'^docs/', include('rest_framework_swagger.urls')),

 ) + urlpatterns
