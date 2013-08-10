# coding: utf-8


def register_views(app, *view_modules):
    for v in view_modules:
        app.register_blueprint(v.bp)
        if hasattr(v, 'setup'):
            v.setup(app)


