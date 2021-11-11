class Config:
    """
    parent configuration class
    """
    SECRET_kEY = 'felix'

    DEBUG = True

class Prodconfig(Config):
    """
    production configuration
    """

class Devconfig(Config):
    """
    Development configuration
    """
    DEBUG = True
config_options={
    'development':Devconfig,
    'production': Prodconfig
}