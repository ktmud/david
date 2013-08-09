# coding: utf-8
import logging

from lib.session import RedisSessionInterface
from lib.utils import setup_logging

from flask import Flask, render_template
import config

setup_logging()


app = Flask(__name__)
app.session_interface = RedisSessionInterface(prefix='dawei:session')

app.config.from_object(config)

from view import misc, admin

app.register_blueprint(misc.bp)
app.register_blueprint(admin.bp)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(403)
def not_allowed(error):
    return render_template('errors/403.html'), 403

if __name__ == '__main__':
    app.run(
        debug=config.DEBUG
    )
