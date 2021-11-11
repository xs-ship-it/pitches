from flask import Flask
from config import config_options


def create_app(config_name):
    # initializing flask extension
    app = Flask(__name__)
    
    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    #registering blueprints
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app
    