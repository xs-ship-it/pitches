from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

  # initializing flask extension
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
  
    
    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    #registering blueprints
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app
    
    
