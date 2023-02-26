from dataclasses import asdict
from typing import Union

from faunadb import query
from faunadb.client import FaunaClient

from core.domain.data_objects import QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto
from core.services.database_saver import DatabaseSaver


class FaunaDatabaseSaver(DatabaseSaver):
    def __init__(self, client: FaunaClient, collection: str):
        self.client = client
        self.collection = collection

    def save(self, dto: Union[QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto]):
        self.client.query(
            query.create(
                query.collection(self.collection), {
                    'data': asdict(dto)
                }
            )
        )
