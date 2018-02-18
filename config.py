""" Base config file
REQUIREMENTS :
Need from config import Config

SETUP :
Shell variable creation  :  $ export FLASK_ENV="DevelopmentConfig"
Get  config option  : config_name = os.getenv('FLASK_ENV', 'TestConfig')
Object-based default configuration : app.config.from_object(config[config_name])
Located in /instance folders configuration for extra/hidden parameter : app.config.from_pyfile('config.cfg', silent=True)

USAGE :
Can access the configuration variables: app.config["VAR_NAME"].

 """

# TODO Set env and default for all parameter

import logging
import os
from os.path import abspath, dirname, join
from base64 import b64encode
from os import urandom


_cwd = dirname(abspath(__file__))


class Config(object):
    # global  flask parameter
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default=b64encode(urandom(64)).decode('utf-8'))

    # REST parameter
    SWAGGER_UI_JSONEDITOR = True

    # data and database parameter
    DATA_DIRECTORY = join(_cwd, 'data')
    SQLALCHEMY_DATABASE_NAME = 'moblog.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(DATA_DIRECTORY, SQLALCHEMY_DATABASE_NAME)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SAM Security database
    SQLALCHEMY_SAM_DATABASE_NAME = 'sam.db'
    SQLALCHEMY_BINDS = {'sam': 'sqlite:///' + join(DATA_DIRECTORY, SQLALCHEMY_SAM_DATABASE_NAME)}

    # Logging parameter
    MAIL_SERVER = False
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_PATH = 'logs'
    LOGGING_LEVEL = logging.DEBUG
    LOGFILE = 'affluents.log'

    # form parameter
    WTF_CSRF_ENABLED = False
    WTF_CSRF_SECRET_KEY = b64encode(urandom(64)).decode('utf-8')

    # FTP parameter
    UPLOAD_PHOTO_FOLDER = os.path.join('static', 'data_image')
    FTP_HOST = os.environ.get("FTP_HOST", default="www.noop.com")
    FTP_USERNAME = os.environ.get("FTP_USERNAME", default="user")
    FTP_PASSWORD = os.environ.get("FTP_PASSWORD", default="password")
    FTP_PORT = 22
    FTP_REMOTE_DIRECTORY = '/LSMV3/'
    FTP_REMOTE_DIRECTORY_IMG = 'img/'
    FTP_LOCALE_DIRECTORY = UPLOAD_PHOTO_FOLDER + "/"  # "./static/data_image/"

    # Html gfeneration parameter
    GENARATE_DIRECTORY_OUTPUT = './moblogserver/frontend/output/'
    GENARATE_DIRECTORY_LAYOUT = './generator/'
    GENARATE_LAYOUT = 'post.html'

    # JWT Config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', default=b64encode(urandom(64)).decode('utf-8'))
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    # Without this get_auth_token via POST request w/ JSON data does not work

    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = True
    DATA_DIRECTORY = join(_cwd, 'data/')
    SQLALCHEMY_DATABASE_NAME = 'dev_fieldBlog.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(DATA_DIRECTORY, SQLALCHEMY_DATABASE_NAME)
    MAIL_SERVER = False


class TestConfig(Config):

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'test_fieldBlog.db')
