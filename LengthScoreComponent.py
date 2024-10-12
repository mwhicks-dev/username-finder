from IScoreComponent import IScoreComponent

class LengthScoreComponent(IScoreComponent):

    def __init__(self, max_length: int):
        self.max_length = max_length

    def score_username(self, name: str) -> float:
        return len(name) / self.max_length