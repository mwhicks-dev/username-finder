from abc import ABC, abstractmethod

class IScoreComponent(ABC):

    @abstractmethod
    def score_username(self, name: str) -> float:
        """
        Given a username, provides it a float score on a scale of 1-10.
        """
        pass