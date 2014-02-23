#!/bin/bash
# -*- ENCODING: UTF-8 -*-
cd ~/webapps/exw/exw
python2.7 manage.py collectstatic
cd ~/webapps/static_exw
rm -rf admin/ admin_tools/ fonts/ css/ img/ js/ mce_filebrowser/ stylus/ tiny_mce/
cd ~/webapps/exw/exw/static
cp -r admin/ admin_tools/ fonts/ css/ img/ js/ mce_filebrowser/ tiny_mce/  ~/webapps/static_exw

