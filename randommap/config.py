"""
Configuration variables for different environments.
"""
import os

from . import application


class BaseConfig(object):
    DEBUG = False

    REDIS_URL = os.environ["REDIS_URL"]
    PORT = int(os.environ["PORT"])

    ZOOM = 9
    MAP_TTL = 60  # seconds
    RETINA_IMAGES = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    RETINA_IMAGES = False
    MAP_TTL = 120  # seconds


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MAP_TTL = 1
    RETINA_IMAGES = False


application.config.from_object(
    {"production": ProductionConfig, "development": DevelopmentConfig}.get(
        os.environ["APP_CONFIG"], DevelopmentConfig
    )
)
