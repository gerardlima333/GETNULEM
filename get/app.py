# app/app.py
from flask import Blueprint, render_template
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for


app = Blueprint('app', __name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.column(db.Integer, primary_key= True)
    nome = db.column(db.string(80), nullable=False)
    email = db.column(db.string(120), nullable=False, unique= True)
    
    def __repr__(self):
        return f'<Usuario {self.email}'

db.create_all

    
#@app_bp.route('/adiciona_usuario')
#def criar_usuario():
    

@app.route('/login', methods=['GET'])
def index():
    return render_template('func.html')

@app.route('/m', methods=['POST'])
def menu():
    return render_template('adm.html')

@app.route('/card', methods=['POST'] )
def adicionar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        novo_usuario = Usuario(nome, email)
        db.session.add(novo_usuario)
        db.session.commit()
        
    return redirect(url_for("cad"))
def cad():

    
    
    
    
    
    return render_template('cad.html')


if __name__=="__main__":
    app.run(debug=True)
    
