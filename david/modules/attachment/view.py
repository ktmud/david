# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, request
from david.lib.template import st

from david.core.attachment import Attachment


bp = Blueprint('attachment', __name__)


@bp.route('/api/attachment/<id>', methods=['GET', 'POST', 'DELETE'])
def qiniu_upload(id):
    item = Attachment.get_or_404(id)
    if request.method == 'POST':
        item.update_props(title=request.form.get('title'),
                desc=request.form.get('desc'))
        return jsonify(r=0, item=item.serialize())
    if request.method == 'DELETE':
        item.remove()
        return jsonify(r=0)
    return jsonify(r=0, item=item.serialize())
