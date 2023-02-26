from faunadb.client import FaunaClient

from adapters.fauna_question_extractor import FaunaQuestionExtractor
from adapters.fauna_question_saver import FaunaQuestionSaver
from core.domain.data_objects import QuestionDto, QuestionType, ObjectId
from settings import FAUNA__ADMIN_KEY


class TestFaunaQuestionIntegration:
    fauna_client = FaunaClient(
        secret=FAUNA__ADMIN_KEY,
    )

    sample_question = QuestionDto(
        answer_id=ObjectId('123'),
        attachment=b'123',
        question_price=100,
        question_id=ObjectId('123'),
        question_type=QuestionType.IMAGE.value,
    )

    def test_fauna_question_saver(self):
        saver = FaunaQuestionSaver(
            client=self.fauna_client,
        )
        saver.save(question=self.sample_question)

    def test_fauna_question_extractor(self):
        extractor = FaunaQuestionExtractor(
            client=self.fauna_client,
        )

        result = extractor.extract(question_id=ObjectId('123'))
        expected_result = self.sample_question

        assert result == expected_result
