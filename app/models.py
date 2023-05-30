from . import db


class AttachmentType:
    TEXT = 'text only'
    AUDIO = 'audio uploaded'
    VIDEO = 'video uploaded'
    LINKED = 'link to online audio/video'
    IMAGE = 'image uploaded'


class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.String(64), primary_key=True)
    question_type = db.Column(db.String(64))
    question_price = db.Column(db.Integer)
    question_position = db.Column(db.Integer)
    related_category = db.Column(db.String(64), db.ForeignKey('categories.category_id'))
    text = db.Column(db.Text)
    attachment = db.Column(db.String(64))
    related_answer = db.relationship('Answer', backref='questions', lazy='dynamic')


class Answer(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.String(64), primary_key=True)
    answer_type = db.Column(db.String(64))
    related_question_id = db.Column(db.String(64), db.ForeignKey('questions.question_id'))
    text = db.Column(db.Text)
    attachment = db.Column(db.String(64))


class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.String(64), primary_key=True)
    category_name = db.Column(db.String(64))
    related_questions = db.relationship('Question', backref='categories', lazy='dynamic')
    related_round = db.Column(db.String(64), db.ForeignKey('rounds.round_id'))


class Round(db.Model):
    __tablename__ = 'rounds'
    round_id = db.Column(db.String(64), primary_key=True)
    round_name = db.Column(db.String(64))
    related_categories = db.relationship('Category', backref='rounds', lazy='dynamic')
    related_game = db.Column(db.String(64), db.ForeignKey('games.game_id'))


class Game(db.Model):
    __tablename__ = 'games'
    game_id = db.Column(db.String(64), primary_key=True)
    game_name = db.Column(db.String(64))
    related_rounds = db.relationship('Round', backref='games', lazy='dynamic')
