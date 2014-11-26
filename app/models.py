
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/mydb3'
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__='user'

	id=db.Column(db.Integer, primary_key=True)
	nickname=db.Column(db.String(64),unique=True,index=True)
	email = db.Column(db.String(120), index=True, unique=True)
#	posts = db.relationship('Post', backref='author', lazy='dynamic')
	
	def repr(self):
		return "User %r" % (self.nickname)

	def __init__(self, nickname, email):
		self.nickname = nickname
		self.email = email

class employee(db.Model):
	__tablename__='employee'
	

	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(64),unique=True,index=True)
	contactno=db.Column(db.Integer,unique=True,index=True)
	
	def repr(self):
		return "employee %r" % (self.name)

	def __init__(self, name, contactno):
		self.name = name
		self.contactno=contactno

"""class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


	
	def __repr__(self):
		return '<Post %r>' % (self.body)    """