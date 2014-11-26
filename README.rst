Oaks_Appgeonode
========================

Geonode custom app for Oaks project.


Requirements
------------
It requires Geonode, django-rest-framework, rest_framework_swagger,
django-oauth2-provider, django-cors-headers and oaks_node .

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

    pip install django-cors-headers

Install `oaks_node <https://github.com/pcasciano/oaks_node>`_ following `oaks_node readme <https://github.com/pcasciano/oaks_node/blob/master/README.md>`_

Install rest swgger with::

    git clone https://github.com/pcasciano/django-rest-swagger.git
    
    cd django-rest-swagger
    
    python setup.py install
     
     
Installation
------------
Install oaks_geonode with::

   cd /var/www

   git clone https://github.com/pcasciano/oaks_geonode.git

   cd oaks_geonode

   git submodule init

   git submodule update
   
   python manage.py syncdb
 
   python manage.py collectstatic
   
   cd ..
   
   sudo pip install -e oaks_geonode



Usage
-----

Rename the local_settings.py.sample to local_settings.py and edit it's content by setting the SITEURL and SITENAME.

Edit the file /etc/apache2/sites-available/geonode and change the following directive from:

    WSGIScriptAlias / /var/www/geonode/wsgi/geonode.wsgi

to:

    WSGIScriptAlias / /var/www/oaks_geonode/oaks_geonode/wsgi.py

Restart apache::

     sudo service apache2 restart


Your oaks_geonode app URL is http://localhost



