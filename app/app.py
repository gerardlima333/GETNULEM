# app/app.py
from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__)

@app_bp.route('/login', methods=['GET'])
def index():
    return render_template('func.html')

@app_bp.route('/m', methods=['POST'])
def menu():
    return render_template('adm.html')

@app_bp.route('/card' )
def cad():
    return render_template('cad.html')


if __name__=="__main__":
    app_bp.run(debug=True)
    
