#!/bin/bash

APPNAME=mash_backend
APPDIR=/home/ubuntu/projects/mashdjangobackend/

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPFIR'gunicorn-error.log'

NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=mash_backend.settings.production
ADDRESS=0.0.0.0:8000
echo 'changing dir'
cd $APPDIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
workon $APPNAME

echo 'starting server' 
exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
