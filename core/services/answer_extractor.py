import abc

from core.domain.data_objects import ObjectId


class QuestionExtractor(abc.ABC):
    def extract(self, answer_id: ObjectId):
        ...
