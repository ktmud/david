# -*- coding: utf-8 -*-
from flask import Blueprint, request, g, abort, redirect, url_for
from david.lib.template import st


from .model import Magazine, Photos


bp = Blueprint('gallery', __name__)


perpage = 10


def list_data(mod, page):
    cls = Magazine if 'magazine' == mod else Photos
    pagination = cls.query.order_by(cls.id.desc()).paginate(page, perpage)
    items = [x.serialize() for x in pagination.items]
    return dict(r=0,
            total=pagination.total,
            has_next=pagination.has_next,
            items=items)


@bp.route('/api/gallery/<mod>/p<int:page>')
def api_list(mod='photos', page=1):
    return jsonify(list_data(mod, page))

@bp.route('/api/gallery/<int:id>')
def api_item(id):
    if mod not in ['magazine']:
        return abort(404)
    cls = Magazine if 'magazine' == mod else Photos
    item = cls.get_or_404(id)
    return jsonify(item=item.serialize())


@bp.route('/gallery/<mod>/')
def home(mod):
    if mod not in ['magazine']:
        return abort(404)
    data = list_data(mod=mod, page=1)
    return st('modules/gallery/%s.html' % mod, **locals())


@bp.route('/gallery/<mod>/<int:ident>/')
def show(mod, ident):
    if mod not in ['magazine']:
        return abort(404)
    cls = Magazine if 'magazine' == mod else Photos
    item = cls.get_or_404(ident)
    carousel_items = [dict(img=x['large_url'], caption=x['desc']) for x in item.pics_info()]
    return st('modules/gallery/show.html', **locals())




__all__ = [bp]
