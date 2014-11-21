# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
from geonode.settings import *
#
# General Django development settings
#

INSTALLED_APPS += (
    'rest_framework',
    'rest_framework_swagger',
    'provider',
    'provider.oauth2',
    'oaks_rest_api',
    'corsheaders',
)

MIDDLEWARE_CLASSES += (
    'corsheaders.middleware.CorsMiddleware',
)

SITENAME = 'oaks_geonode'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'geonode',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'geonode',
        'PASSWORD': 'ÇÄüÞÈLÁ8',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    },
   'geonode_imports' : {
       'ENGINE': 'django.contrib.gis.db.backends.postgis',
       'NAME': 'geonode-imports',
       'USER' : 'geonode',
       'PASSWORD' : 'ÇÄüÞÈLÁ8',
       'HOST' : 'localhost',
       'PORT' : '5432',
   }
}


# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/var/www/oaks-data'

WSGI_APPLICATION = "oaks_geonode.wsgi.application"

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'oaks_geonode.urls'

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass
