from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
    
    #oaks_rest_api
    url(r'^', include('oaks_rest_api.urls')),
    #oaks_rest_api swagger
    url(r'^docs/', include('rest_framework_swagger.urls')),
    
 ) + urlpatterns
