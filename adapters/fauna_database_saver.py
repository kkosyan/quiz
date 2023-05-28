from faunadb import query
from faunadb.client import FaunaClient

from core.domain.data_objects import BaseDto
from core.services.database_saver import DatabaseSaver


class FaunaDatabaseSaver(DatabaseSaver):
    def __init__(self, client: FaunaClient):
        self.client = client

    def save(self, dst: str, dto: BaseDto):
        self.client.query(
            query.create(
                query.collection(dst), {
                    'data': dto.as_dict()
                }
            )
        )
