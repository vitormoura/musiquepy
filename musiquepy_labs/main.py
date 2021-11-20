from __context__ import package_path

import os
import logging
import logging.config

def explore_path_info():
    print(PACKAGE_ROOT_DIR)
    print(__file__)


def explore_logging():

    #logging.basicConfig(format="%(levelname)s %(asctime)s -- %(message)s", level=logging.INFO)
    """
    Pour en savoir plus: 
    https://docs.python.org/3/library/logging.html
    https://docs.python.org/3/howto/logging.html

    """

    logging.config.fileConfig(package_path('logging.conf'))

    """
    ch = logging.StreamHandler()
    #ch = logging.NullHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)

    log.setLevel(logging.DEBUG)
    log.addHandler(ch)
    """

    log = logging.getLogger('simpleExample')
    log.info('hello %s', '[error error error]')


if __name__ == '__main__':
    explore_logging()
    # explore_path_info()
