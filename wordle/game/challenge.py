from wordle.models.game import Challenge, Guess, GuessFeedback
from .guess_checker import GuessChecker, DefaultGuessChecker


class ChallengeInstance:

    def __init__(self, challenge: Challenge, guess_checker: GuessChecker):
        self.challenge = challenge
        self.guesses: list[Guess] = []
        self._guess_checker = guess_checker

    def make_guess(self, guess: Guess) -> GuessFeedback:
        self.guesses.append(guess)
        return self._guess_checker.get_feedback(self.challenge, guess)


def create_instance(challenge: Challenge) -> ChallengeInstance:
    return ChallengeInstance(challenge, DefaultGuessChecker())
