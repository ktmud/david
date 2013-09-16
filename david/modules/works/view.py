# -*- coding: utf-8 -*-
from flask import Blueprint, request, g, abort, redirect, url_for
from david.lib.template import st
from .model import *

from ..artist.model import Artist


bp = Blueprint('works', __name__)

@bp.route('/works/')
def home():
    return redirect(url_for('works.list', catname='movie'))
    return st('/modules/works/index.html', **locals())


@bp.route('/work/<uid>/')
def show(uid):
    work = Work.get_or_404(uid)
    audios, videos = work.attachment_medias()
    carousel_items = [dict(img=a.url(), caption=a.desc) for a in work.attachment_pics()]
    cat = work.cat_name
    artist = work.artist
    artist_work_url = artist_work_url_func(work.cat_name)
    return st('/modules/works/%s/show.html' % cat, **locals())


catname2id = {
    'movie': C_MOVIE,
    'music': C_MOVIE,
    'tv': C_TV, 
}

@bp.route('/works/<catname>/')
@bp.route('/works/<catname>/p<int:page>')
def list(catname, page=1):
    cat_id = catname2id.get(catname)
    if not cat_id:
        abort(404)
    page = int(page)
    perpage = 100

    artist_work_url = artist_work_url_func(catname)
    
    artist_id = request.args.get('artist', '')
    artist_id = int(artist_id) if artist_id.isdigit() else None
    artist = Artist.get(artist_id)
    query = Work.query.filter(Work.cat == cat_id).order_by(Work.pubdate.desc())
    if artist_id:
        query = query.filter(Work.artist_id == artist_id)

    def artist_work_url(artist):
        args = dict(catname=catname)
        if artist_id != artist.id:
            args['artist'] = artist.id
        return url_for('works.list', **args)

    pagination = query.paginate(page, perpage)
    items = pagination.items

    years = sorted(set(x.pubdate.year for x in items), reverse=True)

    return st('/modules/works/%s/index.html' % catname, **locals())




def artist_work_url_func(catname):
    def func(artist):
        args = dict(catname=catname)
        args['artist'] = artist.id
        return url_for('works.list', **args)
    return func

__all__ = [bp]
