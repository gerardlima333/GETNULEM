from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    senha = db.Column(db.String(250), unique=True, nullable=False)
    card = db.relationship('Card', backref='perfil', lazy=True)
    def __repr__(self):
        return f'<Usuario {self.nome}>'
    
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dieta = db.Column(db.String(300), nullable= True)
    hora = db.Column(db.String(100), unique= False, nullable= False)    
    livre = db.Column(db.String(100), unique= False, nullable= True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)



