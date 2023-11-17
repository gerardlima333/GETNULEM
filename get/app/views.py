from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Usuario
from app import db

app_bp = Blueprint('app', __name__)


@app_bp.route('/')
def index():
    usuarios = Usuario.query.all()

# Criação de um novo usuário
    novo_usuario = Usuario(nome='gerard', email='emai.email.com', senha='gegeca22')

# Adiciona o usuário à sessão
    db.session.add(novo_usuario)

# Realiza o commit para salvar no banco de dados
    db.session.commit()

    return render_template('cad.html', usuarios=usuarios)


@app_bp.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'GET':
        nome = request.form['nome']
        email = request.form['email']
        senha= request.form['senha']
        
               
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return "usuario adicinado."
        


    return redirect(url_for('app.index'))

@app_bp.route('/most', methods=['GET', 'POST'])
def most():
    usuarios = Usuario.query.all()

    return render_template('most.html', usuarios=usuarios)
    



