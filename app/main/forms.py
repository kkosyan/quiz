from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField


class CreateNewGameForm(FlaskForm):
    game_name = StringField('New game name', validators=[DataRequired()])
    submit = SubmitField('Submit')
