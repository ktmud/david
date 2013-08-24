# coding: utf-8

KINDS = {}

def add_kind(kind_id, cls):
    kind_id = str(kind_id)
    if kind_id in KINDS:
        raise RuntimeError('kind id %s already in use' % kind_id)
    KINDS[kind_id] = cls

def get_obj(kind, ident):
    kind = str(kind)
    if kind in KINDS:
        return KINDS[kind].get(ident)
