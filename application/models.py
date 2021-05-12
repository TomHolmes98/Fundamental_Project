from wtforms.fields.simple import SubmitField
from application import db

class Players(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.column(db.String(50), nullable=False)
    position = db.column(db.string(50), nullable=False)
    team_id = db.column(db.Integer, db.ForeignKey('team.id'), nullable=False)

class Team(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50), nullable=False)
    league = db.Column(db.string(50), nullable=False)
    players = db.relationship('Players', backref='team')



    



