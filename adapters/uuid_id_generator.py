from uuid import uuid4

from core.domain.data_objects import ObjectId
from core.services.id_generator import IdGenerator


class UuidIdGenerator(IdGenerator):
    def generate(self) -> ObjectId:
        return ObjectId(str(uuid4()))
