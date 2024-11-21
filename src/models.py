from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    __tablename__ = 'Character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    eye_color = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "birth_date": self.birth_date,
            # do not serialize the password, its a security breach
        }