import abc

from core.domain.data_objects import BaseDto, ObjectId


class DatabaseExtractor(abc.ABC):
    def extract(self, object_id: ObjectId) -> BaseDto:
        ...
