from flask import Flask
from flask import render_template
App = Flask(__name__)



@App.route('/')
def index():
    return render_template('func.html')


if __name__=="__main__":
    
    App.run(debug= True)

