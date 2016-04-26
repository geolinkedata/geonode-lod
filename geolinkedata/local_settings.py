
# -*- coding: utf-8 -*-
import os
import geonode

# Setting debug to true makes Django serve static media and
# present pretty error pages.
DEBUG = True
TEMPLATE_DEBUG = True

# Set to True to load non-minified versions of (static) client dependencies
# Requires to set-up Node and tools that are required for static development 
# otherwise it will raise errors for the missing non-minified dependencies
DEBUG_STATIC = False

SITENAME = 'GeoNode'
SITEURL = "http://localhost/"

#DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_ENGINE = 'postgis'
DATABASE_NAME = 'geonode'
DATABASE_USER = 'geonode'
DATABASE_PASSWORD = 'geonode'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}


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
        'DATASTORE': 'datastore',
    }
}

LANGUAGE_CODE = 'en'

MEDIA_ROOT = '/var/www/geolinkedata-data'
#MEDIA_ROOT = '/var/www/geonode/uploaded/'
STATIC_ROOT = '/var/www/geonode/static/'

# secret key used in hashing, should be a long, unique string for each
# site.  See http://docs.djangoproject.com/en/1.2/ref/settings/#secret-key
SECRET_KEY = 'WcZagJK1Y17ONqPfUq'


CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# A Google Maps API key is needed for the 3D Google Earth view of maps
# See http://code.google.com/apis/maps/signup.html
GOOGLE_API_KEY = ''

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
    '/etc/geonode/templates',
    '/var/www/geonode-lod/geolinkedata/templates',
    os.path.join(GEONODE_ROOT, 'templates'),
)

# Additional directories which hold static files
STATICFILES_DIRS = [
    '/etc/geonode/media',
    os.path.join(GEONODE_ROOT, 'static'),
]

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
BASE_STORAGE = '/var/www/geolinkedata-data/'
UPLOAD_SHAPE = 'shapes'
UPLOAD_TRIPLE_STORE = 'triple-stores'
ZIP_DIR = 'zip'


#orchestrator settings
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
