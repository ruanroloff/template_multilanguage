import os
#from os import environ, path
#from dotenv import load_dotenv

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    #SQLALCHEMY_ECHO = True    
    
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    #app.config['SECRET_KEY'] = SECRET_KEY
    #SECRET_KEY="powerful secretkey"
    #WTF_CSRF_SECRET_KEY="a csrf secret key"


    #BABEL
    LANGUAGES = ['en', 'de', 'fr']

    
    
        

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<db_url>:<port>/<db_name>"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER= '<mail_sender>'
    MAIL_SERVER= '<mail_smtp_host>'
    MAIL_PORT= '<mail_port>'
    MAIL_USERNAME= '<mail_username>'
    MAIL_PASSWORD= '<mail_password>'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= '<upload_folder>'

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}