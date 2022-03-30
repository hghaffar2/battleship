from battleship.api import db


class Battleship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(120), nullable=False)
