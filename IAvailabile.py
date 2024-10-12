from abc import ABC, abstractmethod

class IAvailable(ABC):

    @abstractmethod
    def is_username_available(self, name: str) -> bool:
        pass