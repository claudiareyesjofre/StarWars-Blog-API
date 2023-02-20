from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self): 
        return ' %r' % self.email
    #esta funcion representation es para que al traer info de base de datos pueda
    #identificarlo de alguna manera, en este caso con el email
    #el usuario xxx@gmail.com (fx solo se verá si haces print) para identificar o reconocer.BaseException()  
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    #esta funcion serialize sirve para cuando traigas por ejemplo todos los
    # usuarios de la base de datos me entregue la info que yo quiero, en este
    # caso el id y el email, uno no pide la pasword, para que cuando alguien 
    # llame a la clase usuario te retorne info valiosa, no la clave
    #
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return'<Character %r>' % self.name

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
        }

    
class Fav_Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(300), db.ForeignKey("character.name"))
    user_fav = db.Column(db.String(300), db.ForeignKey("user.email"))  
    rel_character = db.relationship("Character")
    rel_user = db.relationship("User")  

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return'<Planet %r>' % self.name

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
        }

    
class Fav_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(300), db.ForeignKey("planet.name"))
    user_fav = db.Column(db.String(300), db.ForeignKey("user.email"))  
    rel_planet = db.relationship("Planet")
    rel_user = db.relationship("User")  
     

  