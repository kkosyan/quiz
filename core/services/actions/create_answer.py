from typing import Optional

from core.domain.data_objects import AnswerType, AnswerDto, QuestionDto
from core.services.id_generator import IdGenerator


class AnswerCreator:
    def __init__(self, id_generator: IdGenerator):
        self.id_generator = id_generator

    def create(self, answer_type: AnswerType, question: QuestionDto, attachment: Optional[bytes] = None,
               text: Optional[str] = None):
        answer_id = self._generate_question_id()
        return AnswerDto(
            answer_id=answer_id,
            attachment=attachment,
            text=text,
            answer_type=answer_type,
            question_id=question.question_id,
            answer_price=question.question_price,
        )

    def _generate_question_id(self):
        return self.id_generator.generate()
