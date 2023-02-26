from typing import Union, Type

from faunadb import query
from faunadb.client import FaunaClient

from core.domain.data_objects import ObjectId, QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto
from core.services.database_extractor import DatabaseExtractor


class FaunaDatabaseExtractor(DatabaseExtractor):
    def __init__(self, client: FaunaClient, index: str, collection: str,
                 dto: Union[Type[QuestionDto], Type[AnswerDto], Type[TaskDto], Type[RoundDto], Type[GameDto]]):
        self.client = client
        self.index = index
        self.collection = collection
        self.dto = dto

    def extract(self, object_id: ObjectId) -> Union[QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto]:
        object = self.client.query(
            query.paginate(
                query.match(query.index(self.index), object_id),
            ),
        )
        object_data = self.client.query(
            query.get(
                query.ref(query.collection(self.collection), object['data'][0].id())
            )
        )['data']

        return self.dto.build(**object_data)
