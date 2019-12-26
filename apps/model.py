from flask_sqlalchemy import SQLAlchemy
from apps import app

db = SQLAlchemy(app)


class Goods(db.Model):
    __tablename__ = 't_goods'
    id = db.Column(db.Integer, primary_key=True)
    gname = db.Column(db.String(80), unique=True)
    gtype = db.Column(db.String(2))
    gprice = db.Column(db.String(5))
    gage =db.Column(db.Integer)

