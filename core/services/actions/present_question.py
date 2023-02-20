from typing import Optional

from core.domain.data_objects import QuestionDto, ObjectId, Attachment, QuestionType


class QuestionPresenter:
    def __init__(self, question_id: ObjectId):
        self.question_id = question_id

    def present(self, question_type: QuestionType, answer_id: ObjectId, text: Optional[str],
                attachment: Optional[Attachment]):
        return QuestionDto(
            question_id=self.question_id,
            text=text,
            attachment=attachment,
            question_type=question_type,
            answer_id=answer_id,
        )
