from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PlayersForm(FlaskForm):
    name=StringField('Enter Player Name', validators=[DataRequired()])
    nationality=StringField('Enter Player Nationality', validators=[DataRequired()])
    position=StringField('Enter Player Position', validators=[DataRequired()])
    submit=SubmitField('Add Player')

class TeamForm(FlaskForm):
    name=StringField('Enter Team Name', validators=[DataRequired()])
    league=StringField('Enter Team League', validators=[DataRequired()])
    submit=SubmitField('Add Team')

