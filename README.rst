GeoLinkeData GeoNode App
========================

GeoNode custom app for GeoLinkeData project.

Requirements
------------

It requires Geonode, django-rest-framework, rest_framework_swagger,
django-oauth2-provider, django-cors-headers and orchestrator .

Install geonode with::

    sudo apt-get update
    
    sudo apt-get install python-software-properties
    
    sudo add-apt-repository ppa:geonode/release
    
    sudo apt-get update
    
    sudo apt-get install geonode
    
    sudo su root
    
    geonode createsuperuser
    
    sudo geonode-updateip 127.0.0.1



Install others django packages with::

    pip install django-oauth2-provider

    pip install djangorestframework
    
    pip install django-rest-swagger

    pip install django-cors-headers

Install `orchestrator <https://github.com/geolinkedata/orchestrator>`_ following `orchestrator readme <https://github.com/geolinkedata/orchestrator/blob/master/README.md>`_       
     
Installation
------------
Install geonode-lod with::

   cd /var/www

   git clone https://github.com/geolinkedata/geonode-lod.git

   cd geonode-lod

   git submodule init

   git submodule update
   
   python manage.py syncdb
 
   python manage.py collectstatic
   
   cd ..
   
   sudo pip install -e geonode-lod

Usage
-----

Rename the local_settings.py.sample to local_settings.py and edit it's content by setting the SITEURL and SITENAME.

Edit the file /etc/apache2/sites-available/geonode and change the following directive from:

    WSGIScriptAlias / /var/www/geonode/wsgi/geonode.wsgi

to:

    WSGIScriptAlias / /var/www/geonode-lod/geolinkedata/wsgi.py

Restart apache::

     sudo service apache2 restart

Your geonode-lod app URL is http://localhost



