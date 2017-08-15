# pylint: disable=too-few-public-methods
"""
Configuration variables for different environments
"""
import os


class BaseConfig(object):
    DEBUG = False

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = os.environ['REDIS_PORT']
    REDIS_DB = 0

    APP_PORT = os.environ['APP_PORT']
    APP_DIR = os.environ['APP_DIR']
    MAPS_DIR = os.path.join(APP_DIR, 'maps')

    MAP_EXPIRE_TIME = 60 # seconds

class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
