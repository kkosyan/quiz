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
    question_price = db.Column(db.String(64))
    text = db.Column(db.String(64))
    attachment = db.Column(db.String(64))

class Answer(db.Model):
    __tablename__ = 'questions'
    answer_id = db.Column(db.String(64), primary_key=True)
    answer_type = db.Column(db.String(64))
    question_id = db.Column(db.String(64))
    text = db.Column(db.String(64))
    attachment = db.Column(db.String(64))

