from flask import Flask
from flask import render_template
App = Flask(__name__)



@App.route('/login')
def index():
    return render_template('func.html')
@App.route('/menu')
def menu():
    return render_template('adm.html')

if __name__=="__main__":
    
    App.run(debug= True)
