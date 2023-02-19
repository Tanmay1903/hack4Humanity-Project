from flask import Flask, request, jsonify, make_response
# from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__, template_folder='../templates')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Tssql1903@127.0.0.1:3306/hack4humanity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["DEBUG"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from app import person_controller






