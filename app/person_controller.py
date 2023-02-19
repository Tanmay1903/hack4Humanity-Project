from flask import Flask, request, jsonify, make_response, render_template
from .models.person_model import Person, NGO
from app import app, db

class PersonController:
    @staticmethod
    @app.route("/create-user", methods=["POST"])
    def createPersonLocation():
        try:
            json_data = request.get_json()
            description = json_data.get("description")
            address = json_data.get("address")
            lat = json_data.get("lat")
            lon = json_data.get('lon')
            last_seen = json_data.get('last_seen')

            if not lat or not lon:
                return make_response(jsonify({'message': "User Location is required",'status' : 400})), 400
            
            user = Person(
                description = description,
                address = address,
                lat = lat,
                lon = lon,
                last_seen = last_seen
            )
            db.session.add(user)
            db.session.commit()

            return make_response(jsonify({"data": user.toDict(),'status' : 201})), 201
        except Exception as e:
            return make_response(jsonify({'message': str(e),'status' : 400})), 400

    @staticmethod
    @app.route("/get-user", methods=["GET"])
    def getPersons():
        try:
            persons = Person.query.limit(10).all()
            persons_list = []
            locations_list = []
            for person in persons:
                persons_list.append(person.toDict())
            # return make_response(jsonify({"data": persons_list,'status' : 200})), 200
            return render_template("map2.html" ,persons=persons_list)
        except Exception as e:
            return make_response(jsonify({'message': str(e),'status' : 400})), 400


    @staticmethod
    @app.route("/create-ngo", methods=["POST"])
    def createNGO():
        try:
            json_data = request.get_json()
            name = json_data.get("name")
            email = json_data.get("email")
            address = json_data.get("address")
            lat = json_data.get("lat")
            lon = json_data.get('lon')

            if not lat or not lon:
                return make_response(jsonify({'message': "User Location is required",'status' : 400})), 400
            
            ngo = NGO(
                name = name,
                email = email,
                address = address,
                lat = lat,
                lon = lon,
            )
            db.session.add(ngo)
            db.session.commit()

            return make_response(jsonify({"data": ngo.toDict(),'status' : 201})), 201
        except Exception as e:
            return make_response(jsonify({'message': str(e),'status' : 400})), 400

    @staticmethod
    @app.route("/get-ngo", methods=["GET"])
    def getNgos():
        try:
            ngos = NGO.query.limit(10).all()
            ngos_list = []
            for ngo in ngos:
                ngos_list.append(ngo.toDict())
            return make_response(jsonify({"data": ngos_list,'status' : 200})), 200
        except Exception as e:
            return make_response(jsonify({'message': str(e),'status' : 400})), 400