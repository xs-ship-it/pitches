class Config:
    """
    parent configurations class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felix:324b21@localhost/pitchtry'
    SECRET_KEY = "felix"
    DEBUG = True

class Prodconfig(Config):
    """
    production cofiguration
    """


class DevConfig(Config):
    """
    Development configuration
    """
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':Prodconfig,
}