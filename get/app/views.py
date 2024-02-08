from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.models import Usuario, Card
from app import db

app_bp = Blueprint('app', __name__)

@app_bp.route('/adm')   
def mosti():
    return render_template('adm.html')

#criei uma rota para adicionar usuario simples.
@app_bp.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        email= request.form['email']
        if len(email) <= 20:
            mensagem_erro03= "Email nao é valido."
            return render_template('cad.html' ,erro= mensagem_erro03)
        else:
            email= request.form['email']
        nome = request.form['nome']
        senha= request.form['senha']
        if len(senha) <= 7:
            mensagem_erro03= "minimo 8 caracteres para senha."
            return render_template('cad.html', erro= mensagem_erro03)
        else:
            senha= request.form['senha']     

        
               
        novo_usuario = Usuario(nome=nome, email=email, senha= senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return render_template('adm.html')
    return redirect(url_for('app.index'))

@app_bp.route('/login', methods= ['GET','POST'])
def login():
    render_template('log.html')
    usuario = Usuario.query.all()
    
    if request.method == 'POST':
        usus = request.form['nome']
        sens = request.form['senha']
        if any(usus == u.nome and sens == u.senha for u in usuario):
            mensagem_erro2 = f'bem vindo {usus}'
    # Lógica para autenticação bem-sucedida
            return render_template("adm.html", erro= mensagem_erro2, nome = usus, nome_usuario= usus)
        else:
            mensagem_erro = "usuario nao encontrado."
            return render_template('log.html', erro = mensagem_erro)
           
    return render_template('adm.html')

@app_bp.route("/card", methods=['POST', 'GET'])
def c():
    return render_template ('carda.html')

@app_bp.route("/addca", methods=['POST'])

def addcard():
    nome_usuario = request.form['nome_usuario']
    usuario = Usuario.query.filter_by(nome=nome_usuario).first()
    if usuario is None:
        return render_template('carda.html', erro="Usuário não encontrado")
    else:
        if request.method == 'POST':
            dieta = request.form['dieta']        
            hora = request.form['hora']
            livre = request.form['livre']
            usuario_id = usuario.id
       
            novo_card = Card(dieta=dieta, hora=hora, livre=livre, usuario_id = usuario_id)
            db.session.add(novo_card)
            db.session.commit()
        
       
            return render_template('carda.html', sucesso="Card adicionado com sucesso")
                



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
        
        
@app_bp.route('/enter', methods= ['GET', 'POST'])
def rend():
     return render_template('log.html')
