# -*- coding: utf-8 -*-

DEBUG = TEMPLATE_DEBUG = True

DEBUG_STATIC = False

SITENAME = 'GeoNode'
SITEURL = 'http://localhost/'

GEOSERVER_URL = SITEURL + 'geoserver/'

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://localhost:8080/geoserver/',    # GEOSERVER_URL,
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINTNG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIT_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'geonode_imports',
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

MAP_BASELAYERS = [{
    "source": {
        "ptype": "gxp_wmscsource",
        "url": GEOSERVER_URL + "wms",
        "restUrl": "/gs/rest"
     }
  },{
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer",
    "args":["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.OSM",
    "args":["OpenStreetMap"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"osm",
    "group":"background",
    "visibility": True
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"naip",
    "group":"background",
    "visibility": False
  }, {
    "source": {"ptype": "gxp_bingsource"},
    "name": "AerialWithLabels",
    "fixed": True,
    "visibility": False,
    "group":"background"
  },{
    "source": {"ptype": "gxp_mapboxsource"},
  }
]

# Uncomment the following to receive emails whenever there are errors in GeoNode
#ADMINS = (
#            ('John', 'john@example.com'),
#         )

# Uncomment the following to use a Gmail account as the email backend
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'fake@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings




#dirs for upload and storing files
UPLOAD_SHAPE = '/var/www/oaks-data/shapes'
UPLOAD_TRIPLE_STORE = '/var/www/oaks-data/triple-stores'


#oaks_node settings
NODE_HOST = '127.0.0.1'
NODE_PORT = 3000


#rest_framework config
REST_FRAMEWORK = {

   'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.OAuth2Authentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.XMLRenderer',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'default': '10/minute', #10/minute
        'download': '50/minute', #5/minute
        'utility': '5/minute', #5/minute
    }
}

#rest swagger config
SWAGGER_SETTINGS = {
    "exclude_namespaces": [], # List URL namespaces to ignore
    "api_version": '1.0',  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '', # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
}


#CORSheaders settings
CORS_ORIGIN_WHITELIST = (
    'localhost:7999',
    #'127.0.0.1:7999',
)

CORS_ALLOW_METHODS = (
    'GET',
)


#geogigpy settings
GEOGIG_REPO = '/tmp/repos'
