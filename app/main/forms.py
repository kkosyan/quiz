from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, URLField, BooleanField
from wtforms.validators import DataRequired, Optional


class CreateNewGameForm(FlaskForm):
    game_name = StringField('New game name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CreateNewRound(FlaskForm):
    round_name = StringField('Round name:', validators=[DataRequired()])
    start_price = StringField('Start price:', validators=[DataRequired()])

    submit_new_round = SubmitField('Submit new round')


class CreateNewCategory(FlaskForm):
    category_name = StringField('Category name:', validators=[DataRequired()])
    question_1_text = TextAreaField('Text:', validators=[Optional()])
    question_1_file = FileField('File:', validators=[Optional()])
    question_1_url = URLField('URL:', validators=[Optional()])
    question_2_text = TextAreaField('Text:', validators=[Optional()])
    question_2_file = FileField('File:', validators=[Optional()])
    question_2_url = URLField('URL:', validators=[Optional()])
    question_3_text = TextAreaField('Text:', validators=[Optional()])
    question_3_file = FileField('File:', validators=[Optional()])
    question_3_url = URLField('URL:', validators=[Optional()])
    question_4_text = TextAreaField('Text:', validators=[Optional()])
    question_4_file = FileField('File:', validators=[Optional()])
    question_4_url = URLField('URL:', validators=[Optional()])
    question_5_text = TextAreaField('Text:', validators=[Optional()])
    question_5_file = FileField('File:', validators=[Optional()])
    question_5_url = URLField('URL:', validators=[Optional()])

    answer_1_text = TextAreaField('Text:', validators=[Optional()])
    answer_1_file = FileField('File:', validators=[Optional()])
    answer_1_url = URLField('URL:', validators=[Optional()])
    answer_2_text = TextAreaField('Text:', validators=[Optional()])
    answer_2_file = FileField('File:', validators=[Optional()])
    answer_2_url = URLField('URL:', validators=[Optional()])
    answer_3_text = TextAreaField('Text:', validators=[Optional()])
    answer_3_file = FileField('File:', validators=[Optional()])
    answer_3_url = URLField('URL:', validators=[Optional()])
    answer_4_text = TextAreaField('Text:', validators=[Optional()])
    answer_4_file = FileField('File:', validators=[Optional()])
    answer_4_url = URLField('URL:', validators=[Optional()])
    answer_5_text = TextAreaField('Text:', validators=[Optional()])
    answer_5_file = FileField('File:', validators=[Optional()])
    answer_5_url = URLField('URL:', validators=[Optional()])

    submit_category = SubmitField('Submit category')
