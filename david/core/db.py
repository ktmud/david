# coding: utf-8
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import orm, func, sql


db = SQLAlchemy()


class CatLimitedQuery(BaseQuery):

    def __init__(self, *args, **kwargs):
        super(CatLimitedQuery, self).__init__(*args, **kwargs)
        cls = self._entities[0].type
        # only apply filter to cat_id defined
        if hasattr(cls, 'cat'):
            filtered = self.filter(cls.cat==cls.cat_id)
            self._criterion = filtered._criterion



class UidMixin(object):

    uid = db.Column('uid', db.String(255), index=True, unique=True)

    @property
    def slug(self):
        return str(self.uid or self.id)
    
    @classmethod
    def get(cls, ident):
        ident = str(ident)
        if ident.isdigit():
            return cls.query.get(int(ident))
        else:
            return cls.query.filter(cls.uid == ident).first()

    @classmethod
    def gets(cls, idents):
        return [cls.get(i) for i in idents]

