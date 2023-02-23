from typing import Optional

from core.domain.data_objects import AnswerType, QuestionDto, Attachment, AnswerDto, ObjectId


class AnswerPresenter:
    def __init__(self, answer_id: ObjectId):
        self.answer_id = answer_id

    def present(self, answer_type: AnswerType, question: QuestionDto, text: Optional[str],
                attachment: Optional[Attachment]):
        return AnswerDto(
            answer_id=self.answer_id,
            text=text,
            attachment=attachment,
            answer_type=answer_type,
            question_id=question.question_id,
            answer_price=question.question_price,
        )
