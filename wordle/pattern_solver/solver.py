from wordle.models.solution import Solution
from wordle.game_api.challenge import ChallengeProvider


class Solver:

    def __init__(self, challenge: ChallengeProvider):
        self.challenge = challenge

    def solve(self) -> Solution:
        pass
