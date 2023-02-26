from faunadb import query
from faunadb.client import FaunaClient

from core.domain.data_objects import QuestionDto
from core.services.question_saver import QuestionSaver


class FaunaQuestionSaver(QuestionSaver):
    def __init__(self, client: FaunaClient):
        self.client = client

    def save(self, question: QuestionDto):
        self.client.query(
            query.create(
                query.collection('questions'), {
                    'data': {
                        'question_id': question.question_id,
                        'text': question.text,
                        'attachment': question.attachment,
                        'question_type': question.question_type,
                        'answer_id': question.answer_id,
                        'question_price': question.question_price,
                    }
                }
            )
        )
