# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from david.app import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
