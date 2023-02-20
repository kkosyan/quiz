import abc

from core.domain.data_objects import Game


class GameSaver(abc.ABC):
    @abc.abstractmethod
    def save_game(self, game: Game):
        ...
