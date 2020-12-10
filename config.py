import os

class Config:

    BOOKS_URL = 'https://www.googleapis.com/books/v1/volumes?q={}'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tharcissie:ntakarakorwa123@localhost/booklist'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}