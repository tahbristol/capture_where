from datetime import datetime
from project import db, login_manager
from flask_login import UserMixin
from project import ma


@login_manager.user_loader
def load_user(user_id):
 return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    locations = db.relationship('Address', backref='user', lazy=True)
    
    def __repr__(self):
        return "User('{}')".format(self.email)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('email',)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('location', 'user_id')