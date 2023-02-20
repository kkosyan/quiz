from typing import Optional

from core.domain.data_objects import AnswerType, ObjectId, Attachment, AnswerDto


class AnswerPresenter:
    def __init__(self, answer_id: ObjectId):
        self.answer_id = answer_id

    def present(self, answer_type: AnswerType, question_id: ObjectId, text: Optional[str],
                attachment: Optional[Attachment]):
        return AnswerDto(
            answer_id=self.answer_id,
            text=text,
            attachment=attachment,
            answer_type=answer_type,
            question_id=question_id,
        )
