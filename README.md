Explicando La Web
=================

Repositorio donde reside la base del sitio web de explicandolaweb.com.

Montada sobre Django 1.6.1

##Requerimientos:
- pip install -r dev.txt //para requerimientos de desarrollo
- pip install -r deploy.txt //para producción

##Instalación
Si se usa South, realizar las migraciones de las aplicaciones:
- artículos
- tutoriales
- cursos
- blog
- perfiles
- web

##Variables de entorno
Establecer las siguientes variables de entorno
- KEY_DJANGO: Secret key de Django para el archivo de settings
- DB_NAME: con el nombre de la base de datos
- DB_USER: con el nombre de usuario de la base de datos
- DB_PASS: con el password de acceso a la base de datos


