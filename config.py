import os
basedir = os.path.abspath(os.path.dirname(__file__))#telling application where base dir is


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-me'
#secret key = allows for access database or send forms to send info to prevent seasurfing or hacking
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')#if not databse=url, look for database in app.db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
