from typing import Optional

from core.domain.data_objects import QuestionDto, ObjectId, QuestionType


class QuestionPresenter:
    def __init__(self, question_id: ObjectId):
        self.question_id = question_id

    def present(self, question_type: QuestionType, answer_id: ObjectId, question_price: int, text: Optional[str],
                attachment: Optional[bytes]):
        return QuestionDto(
            question_id=self.question_id,
            text=text,
            attachment=attachment,
            question_type=question_type,
            answer_id=answer_id,
            question_price=question_price,
        )
