# coding: utf-8
from david.app import app

if __name__ == '__main__':
    app.run(
        debug=app.config.get('DEBUG')
    )
