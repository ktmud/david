# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from david.lib.template import st

from .model import QiniuAttachment, QiniuUploadFail

bp = Blueprint('qiniu', __name__)

@bp.route('/api/qiniu/upload', methods=['GET', 'POST', 'PUT'])
def qiniu_upload():
    if request.method in ['POST', 'PUT'] and request.files:
        if 'file' not in request.files:
            return jsonify(r=400)
        form = request.form
        owner_id = form.get('owner_id')
        owner_kind = form.get('owner_kind')
        prefix = '%s_%s_' % (owner_kind or 'general', owner_id or '0')
        ret = []
        ok_ids = []

        for k, fp in request.files.iteritems(multi=True):
            if k != 'file':
                continue
            try:
                item = QiniuAttachment.add(fp,
                        name=prefix + fp.filename,
                        mime=fp.mimetype,
                        owner_id=owner_id, owner_kind=owner_kind)
                ret.append(item.serialize())
            except QiniuUploadFail, e:
                ret.append({ 'failure': 'saving', 'filename': fp.filename })
                continue
        return jsonify(r=0, items=ret)


@bp.route('/api/qiniu/callback', methods=['GET', 'POST'])
def qiniu_callback():
    pass
