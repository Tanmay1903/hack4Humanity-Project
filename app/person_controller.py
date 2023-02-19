from flask import Flask, request, jsonify, make_response
from .models.person_model import Person, NGO
from app import app, db

class PersonController:
    @staticmethod
    @app.route("/create-user", methods=["POST"])
    def createPersonLocation():
        json_data = request.get_json()
        description = json_data["description"]
        address = json_data["address"]
        lat = json_data["lat"]
        lon = json_data['lon']
        last_seen = json_data['last_seen']

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