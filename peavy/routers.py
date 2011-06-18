from django.conf import settings

class DjangoDBRouter(object):
    """
    Routes all database operations on peavy models to settings.PEAVY_DATABASE_NAME.

    Peavy has been tested with multiple databases, but South migrations will
    not work. You'll need to manage the tables yourself with syncdb. You should
    be able to make South ignore peavy with this in your settings.py:

        SOUTH_MIGRATION_MODULES = {
            'peavy': 'ignore',
        }

    See:

        http://south.aeracode.org/docs/settings.html#south-migration-modules
        http://south.aeracode.org/ticket/370

    """

    db_name = getattr(settings, 'PEAVY_DATABASE_NAME', 'peavy')

    def db_for_read(self, model, **hints):
        db = None
        if model._meta.app_label == 'peavy':
            db = self.db_name
        return db

    def db_for_write(self, model, **hints):
        db = None
        if model._meta.app_label == 'peavy':
            db = self.db_name
        return db

    def allow_relation(self, obj1, obj2, **hints):
        allow = None
        if obj1._meta.app_label == 'peavy' and obj2._meta.app_label == 'peavy':
            allow = True
        return allow

    def allow_syncdb(self, db, model):
        allow = None
        if db == self.db_name:
            allow = model._meta.app_label == 'peavy'
        elif model._meta.app_label == 'peavy':
            allow = False
        return allow
