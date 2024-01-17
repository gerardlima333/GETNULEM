from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Usuario
from app import db

app_bp = Blueprint('app', __name__)



@app_bp.route('/adicionar_usuario', methods=['GET', 'POST'])

def adicionar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha= request.form['senha']
        
               
        novo_usuario = Usuario(nome=nome, email=email, senha= senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return render_template('adm.html')


    return redirect(url_for('app.index'))


@app_bp.route('/', methods= ['GET'])
def index():
    
    usuarios = Usuario.query.all()
    return render_template('cad.html', usuarios=usuarios)
def adicionar_usuario():
    if request.method == 'GET':
        nome = request.form['nome']
        email = request.form['email']
        senha= request.form['senha']
        
               
        novo_usuario = Usuario(nome=nome, email=email, senha= senha)
        db.session.add(novo_usuario)
        db.session.commit()
    return render_template("adm.html")


@app_bp.route('/most', methods=['GET', 'POST'])
def most():
    usuarios = Usuario.query.all()
    
    

    return render_template('most.html', usuarios=usuarios)

@app_bp.route('/delete/<int:usuario_id>', methods=['POST', 'GET'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)

    if usuario:
        db.session.delete(usuario)
        db.session.commit()

    return redirect(url_for('app.most'))
        

@app_bp.route('/login')
def login():
    return render_template('func.html')


@app_bp.route('/adm')

def mosti():
    return render_template('adm.html')