from sqlalchemy.orm import backref
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash



# @login_manager.user_loader
