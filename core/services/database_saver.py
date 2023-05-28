import abc

from core.domain.data_objects import BaseDto


class DatabaseSaver(abc.ABC):
    def save(self, dst: str, dto: BaseDto):
        ...
