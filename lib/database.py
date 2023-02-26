import abc


class Database(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        ...
