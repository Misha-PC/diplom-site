
class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:111111@localhost/test'