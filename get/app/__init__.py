from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.views import app_bp
app.register_blueprint(app_bp)

from app.models import Usuario  # Certifique-se de criar models.py com a definição do modelo
with app.app_context():
    db.create_all()
