# coding: utf-8
from flask import json, abort
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import orm, func, sql


db = SQLAlchemy()


class CatLimitedQuery(BaseQuery):

    def __init__(self, *args, **kwargs):
        super(CatLimitedQuery, self).__init__(*args, **kwargs)
        cls = self._entities[0].type
        # only apply filter to cat_id defined
        if hasattr(cls, 'cat') and hasattr(cls, 'cat_id') and cls.cat_id:
            filtered = self.filter(cls.cat==cls.cat_id)
            self._criterion = filtered._criterion

    def get(self, *args, **kwargs):
        self._criterion = None
        ret = super(CatLimitedQuery, self).get(*args, **kwargs)
        if hasattr(ret, 'cat'):
            if ret.cat != ret.cat_id:
                return None
        return ret



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
    def get_or_404(cls, ident):
        ret = cls.get(ident)
        if not ret:
            abort(404)
        return ret

    @classmethod
    def gets(cls, idents):
        return [cls.get(i) for i in idents]


class SerializeMixin(object):

    def serialize(self, with_props=True):
        d = {}
        if hasattr(self, '__table__'):
            for c in self.__table__.columns:
                d[c.name] = getattr(self, c.name)
        if hasattr(self, 'props'):
            d.update(self.props)
        return d

    def to_json(self):
        return json.dumpls(self.serialize())

