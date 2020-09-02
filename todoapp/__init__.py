from flask import Flask
from .extensions import mongo
from .main.routes import main

def create_app():
    app = Flask(__name__)
    # mongodb+srv://Admin:<password>@cluster0.yruh1.mongodb.net/<dbname>?retryWrites=true&w=majority
    app.config['MONGO_URI'] = 'mongodb+srv://Admin:<password>@cluster0.yruh1.mongodb.net/<dbname>?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
