import abc

from core.domain.data_objects import ObjectId, QuestionDto


class QuestionExtractor(abc.ABC):
    def extract(self, question_id: ObjectId) -> QuestionDto:
        ...
