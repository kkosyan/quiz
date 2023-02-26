from faunadb.client import FaunaClient

from adapters.fauna_database_extractor import FaunaDatabaseExtractor
from adapters.fauna_database_saver import FaunaDatabaseSaver
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
        saver = FaunaDatabaseSaver(
            client=self.fauna_client,
            collection='questions',
        )
        saver.save(dto=self.sample_question)

    def test_fauna_question_extractor(self):
        extractor = FaunaDatabaseExtractor(
            client=self.fauna_client,
            collection='questions',
            dto=QuestionDto,
            index='question_id',
        )

        result = extractor.extract(object_id=ObjectId('123'))
        expected_result = self.sample_question

        assert result == expected_result
