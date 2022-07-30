from collections.abc import Sequence
from random import randint
from wordle.models.game import Guess


class GuessSelector:

    def select_guess(self, candidates: Sequence[str]) -> Guess:
        pass


class GuessFirstSelector(GuessSelector):

    def select_guess(self, candidates: Sequence[str]) -> Guess:
        return Guess(candidates[0])


class GuessRandomSelector(GuessSelector):

    def select_guess(self, candidates: Sequence[str]) -> Guess:
        index = randint(0, len(candidates) - 1)
        return Guess(candidates[index])
