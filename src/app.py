from flask import Flask
from src.database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://prdenermatos:321@localhost:3306/db'
    db.init_app(app)
    return app

app = create_app()


from src.controller import *