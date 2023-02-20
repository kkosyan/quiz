import abc

from core.domain.data_objects import Attachment


class AttachmentSaver(abc.ABC):
    @abc.abstractmethod
    def save_attachment(self, attachment: Attachment):
        ...
