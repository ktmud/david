# David - A Flask CMS with SQLAlchemy

The CMS behind http://www.tongdawei.cc


## TODO:

1. more generic templates
2. more generic static files handling
3. provide modules as plugin


### Decisions I made

1. make modules as pluggable as possible, see `david/modules`
2. implemented qiuniu CDN attachment upload and its Flask-admin interface
3. use Flask-babel for locale
4. use `alembic` for database schema versioning 
5. use `grunt` to build static files
6. use `fabric` for deployment
