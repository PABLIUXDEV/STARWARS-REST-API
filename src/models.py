from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # favorites = db.relationship('Favorite', back_populates='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # "favorites": [favorite.to_dict() for favorite in self.favorites]
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

class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "climate": self.climate,
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    cargoCapacity = db.Column(db.String(100), nullable=False)
    length = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.model

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "cargoCapacity": self.cargoCapacity,
            "length": self.length,
            # do not serialize the password, its a security breach
        }

# class Favorite(db.Model):
#     __tablename__ = 'Favorite'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
#     character_id = db.Column(db.Integer, db.ForeignKey('Character.id'), nullable=False)
#     # planet_id = db.Column(db.Integer, db.ForeignKey('Planets.id'), nullable=True)
#     # vehicles_id = db.Column(db.Integer, db.ForeignKey('Vehicles.id'), nullable=True)

#     user = db.relationship('User', back_populates='favorites')
#     character = db.relationship('Character', lazy='joined')
#     # planet = db.relationship('Planets', lazy='joined')    
#     # vehicle = db.relationship('Vehicles', lazy='joined')    
    
    # def __repr__(self):
    #     return '<Favorite %r>' % self.model

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "user_id": self.user_id,
    #         "character": self.characters.to_dict() if self.characters else none,
            # "planet": self.planet.to_dict() if self.planet else none,
            # "vehicle": self.vehicle.to_dict() if self.vehicle else none
            # do not serialize the password, its a security breach
        # }
