from app.setup_db import db
from marshmallow import Schema, fields
from sqlalchemy import Column


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
