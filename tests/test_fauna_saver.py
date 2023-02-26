from faunadb.client import FaunaClient

from adapters.fauna_question_saver import FaunaQuestionSaver
from core.domain.data_objects import QuestionDto, QuestionType, ObjectId


class TestFaunaQuestionSaver:
    fauna_client = FaunaClient(
        secret='fnAE9gazHRACWjF_GuNlZZPAI6KV_xxyivottYVQ',
    )

    sample_question = QuestionDto(
        answer_id=ObjectId('123'),
        attachment=b'123',
        question_price=100,
        question_id=ObjectId('123'),
        question_type=QuestionType.IMAGE.value,
        text=None,
    )

    def test_fauna_question_saver(self):
        saver = FaunaQuestionSaver(
            client=self.fauna_client,
        )
        saver.save(question=self.sample_question)
