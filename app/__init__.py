from flask import Flask, request, jsonify, make_response
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/hack4humanity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
# db.create_all()


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config["MYSQL_DB"] = 'flask'

# mysql = MySQL(app)
# conn = mysql.connect()
# cursor = conn.cursor()

if __name__ == '__main__':
    app.run(debug=True)

from app import person_controller






