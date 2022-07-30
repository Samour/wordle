from typing import Union
from wordle.models.game import Challenge, Guess, GuessFeedback, CharFeedback, ChallengeStatus, GuessNotAWord
from .dictionary import Dictionary
from .guess_checker import GuessChecker, DefaultGuessChecker


_GUESS_CORRECT = GuessFeedback([ CharFeedback.CORRECT ] * 5)


class ChallengeInstance:

    def __init__(self, challenge: Challenge, dictionary: Dictionary, guess_checker: GuessChecker):
        self.challenge = challenge
        self.guesses: list[Guess] = []
        self._dictionary = dictionary
        self._guess_checker = guess_checker
        self.challenge_status = ChallengeStatus.IN_PROGRESS

    def make_guess(self, guess: Guess) -> Union[GuessFeedback, GuessNotAWord]:
        if not self._dictionary.contains_word(guess.guess):
            return GuessNotAWord()

        self.guesses.append(guess)
        feedback = self._guess_checker.get_feedback(self.challenge, guess)
        self._update_status(feedback)

        return feedback

    def _update_status(self, feedback: GuessFeedback) -> None:
        if feedback == _GUESS_CORRECT:
            self.challenge_status = ChallengeStatus.SOLVED
        elif len(self.guesses) >= self.challenge.guess_limit:
            self.challenge_status = ChallengeStatus.FAILED


def create_instance(challenge: Challenge, dictionary: Dictionary) -> ChallengeInstance:
    return ChallengeInstance(challenge, dictionary, DefaultGuessChecker())
