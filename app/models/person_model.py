# from .base_model import Model
from app import db
from sqlalchemy_utils.types import UUIDType
import uuid
import datetime

class Person(db.Model):
    id = db.Column(UUIDType, primary_key=True,default = uuid.uuid4)
    description = db.Column(db.String(300), nullable = True)
    address = db.Column(db.String(100), nullable = True)
    lat = db.Column(db.String(100), nullable = True)
    lon = db.Column(db.String(100), nullable = True)
    last_seen = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    is_helped =  db.Column(db.Boolean,default = False)
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def toDict(self):
        json_dict = {
            "id": str(self.id),
            "description": self.description,
            "address": self.address,
            "lat": self.lat,
            "lon": self.lon,
            "last_seen": self.last_seen,
            "is_helped": self.is_helped,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return json_dict

class NGO(db.Model):
    id = db.Column(UUIDType, primary_key=True,default = uuid.uuid4)
    name = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(100), unique = True)
    address = db.Column(db.String(100), nullable = True)
    lat = db.Column(db.String(100), nullable = True)
    lon = db.Column(db.String(100), nullable = True)
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def toDict(self):
        json_dict = {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "lat": self.lat,
            "lon": self.lon,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return json_dict