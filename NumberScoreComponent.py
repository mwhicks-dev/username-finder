from IScoreComponent import IScoreComponent

class NumberScoreComponent(IScoreComponent):

    def score_username(self, name: str) -> float:
        if any(c.isdigit() for c in name):
            return 0
        return 1