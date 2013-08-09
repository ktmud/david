# coding: utf-8
import logging

def setup_logging():
    formatter = logging.Formatter('%(asctime)s %(process)d [%(levelname)s] %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    stdout = logging.StreamHandler()
    stdout.setFormatter(formatter)
    logging.getLogger('').addHandler(stdout)
    logging.getLogger().setLevel(logging.DEBUG)


