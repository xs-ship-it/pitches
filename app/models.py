from sqlalchemy.orm import backref
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
        return User.query.get(user_id)

class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    category= db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    
def save_pitch(self):
    db.session.add(self)
    db.session.commit(self)
    
class comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    
def save_comment(self):
    db.session.add(self)
    db.session.commit(self)
    
class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    avatar = db.Column(db.String)
     
def save_user(self):
    db.session.add(self)
    db.session.commit(self)
    
  
    
@property
def password(self):
        raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self,password):
        self.pass_secure = generate_password_hash(password)

def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

def __repr__(self):
        return f'User {self.username}'
    
    