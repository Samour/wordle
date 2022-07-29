from random import randint
from wordle.models.game import Challenge
from .dictionary import Dictionary


class ChallengeGenerator:

    def __init__(self, dictionary: Dictionary):
        self._dictionary = dictionary

    def generate_challenge(self) -> Challenge:
        random_idx = randint(0, len(self._dictionary.words) - 1)
        return Challenge(self._dictionary.words[random_idx].strip())
