import abc

from core.domain.data_objects import Attachment


class AttachmentExtractor(abc.ABC):
    @abc.abstractmethod
    def get_attachment(self, id: str) -> Attachment:
        ...
