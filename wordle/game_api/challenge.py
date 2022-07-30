from typing import Union
from wordle.models.game import Challenge, ChallengeStatus, Guess, GuessFeedback, GuessNotAWord


class ChallengeProvider:

    def __init__(self):
        self.challenge: Challenge
        self.guesses: list[Guess]
        self.challenge_status: ChallengeStatus

    def make_guess(self, guess: Guess) -> Union[GuessFeedback, GuessNotAWord]:
        pass
