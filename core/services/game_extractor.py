import abc

from core.domain.data_objects import Game


class GameSaver(abc.ABC):
    @abc.abstractmethod
    def extract_game(self, game: Game):
        ...
