import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    WTF_CSRF_ENABLED = True
    REDIS_URL = 'redis://redis:6379/0'
    QUEUES = ['default']

class DevelopmentConfig(object):
    DEBUG = True
    WTF_CSRF_ENABLED = False

class TestingConfig(object):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(object):
    DEBUG = False