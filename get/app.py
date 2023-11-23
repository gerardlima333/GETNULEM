from app import app
from flask import Flask
from flask_migrate import MigrateCommand



if __name__ == '__main__':
    app.run(debug=True)

