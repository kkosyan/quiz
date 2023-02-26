from faunadb.client import FaunaClient

from lib.database import Database


class FaunaDatabase(Database):
    def __init__(self, secret: str):
        self.secret = secret

    def connect(self):
        return FaunaClient(
            secret=self.secret,
        )
