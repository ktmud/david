# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, request
from david.lib.template import st

from david.core.attachment import Attachment
from david.core.accounts.utils import require_editor


bp = Blueprint('attachment', __name__)


@bp.route('/api/attachment/<id>', methods=['GET', 'POST', 'DELETE'])
@require_editor
def qiniu_upload(id):
    item = Attachment.get_or_404(id)
    if request.method == 'POST':
        props = {}
        for k in ('a-desc', 'a-title'):
            if k in request.form:
                props[k.replace('a-', '')] = request.form[k]
        item.update_props(**props)
        return jsonify(r=0, item=item.serialize())
    if request.method == 'DELETE':
        item.remove()
        return jsonify(r=0)
    return jsonify(r=0, item=item.serialize())
