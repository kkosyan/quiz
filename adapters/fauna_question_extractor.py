from faunadb import query
from faunadb.client import FaunaClient

from core.domain.data_objects import ObjectId, QuestionDto
from core.services.question_extractor import QuestionExtractor


class FaunaQuestionExtractor(QuestionExtractor):
    def __init__(self, client: FaunaClient):
        self.client = client

    def extract(self, question_id: ObjectId) -> QuestionDto:
        question = self.client.query(
            query.paginate(
                query.match(query.index('question_id'), question_id),
            ),
        )
        question_data = self.client.query(
            query.get(
                query.ref(query.collection('questions'), question['data'][0].id())
            )
        )['data']

        return QuestionDto(**question_data)
