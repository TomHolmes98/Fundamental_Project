from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    nationality = db.Column(db.String(50), nullable = False)
    position = db.Column(db.String(50), nullable = False)
    teamid = db.Column(db.Integer, db.ForeignKey('team.id'), nullable = True)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    league = db.Column(db.String(50), nullable = False)
    players = db.relationship('Players', backref = 'team')



    



