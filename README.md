# ddsite
cms like backend for company presentation site

###How To

libspatialite and gdal libraries needs to be installed on your machine

also depending on your system might require to change 
```SPATIALITE_LIBRARY_PATH``` in settings.py

```aidl
    ./manage.py migrate --run-syncdb
    ./manage.py createsuperuser
    ./manage.py sample_data
    ./manage.py runserver_plus
```
