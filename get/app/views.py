from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Usuario
from app import db

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('cad.html', usuarios=usuarios)

@app_bp.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'GET':
        nome = request.form['nome']
        email = request.form['email']
        
        print(f'Dados Recebidos: Nome - {nome}, Email - {email}')

        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()

    return redirect(url_for('app.index'))




