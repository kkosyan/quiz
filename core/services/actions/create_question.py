from typing import Optional

from core.domain.data_objects import QuestionDto, Attachment, QuestionType, ObjectId
from core.services.id_generator import IdGenerator


class QuestionCreator:
    def __init__(self, id_generator: IdGenerator):
        self.id_generator = id_generator

    def create(self, question_type: QuestionType, answer_id: ObjectId, question_price: int,
               attachment: Optional[Attachment] = None,
               text: Optional[str] = None):
        question_id = self._generate_question_id()
        return QuestionDto(
            question_id=question_id,
            attachment=attachment,
            text=text,
            question_type=question_type,
            answer_id=answer_id,
            question_price=question_price,
        )

    def _generate_question_id(self):
        return self.id_generator.generate()
