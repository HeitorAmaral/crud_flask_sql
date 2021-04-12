import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Class to put on the default configurations of the application.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Class to put on the Production configurations of the application.
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Class to put on the Development configurations of the application.
    """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """
    Class to put on the Testing configurations of the application.
    """
    TESTING = True
