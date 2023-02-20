import abc

from core.domain.data_objects import ObjectId


class IdGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self) -> ObjectId:
        ...
