# coding: utf-8
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import orm, func, sql


class CatLimitedQuery(BaseQuery):

    def __init__(self, *args, **kwargs):
        super(CatLimitedQuery, self).__init__(*args, **kwargs)
        cls = self._entities[0].type
        # only apply filter to cat_id defined
        if cls.cat_id:
            filtered = self.filter(cls._cat_id==cls.cat_id)
            self._criterion = filtered._criterion

db = SQLAlchemy()
