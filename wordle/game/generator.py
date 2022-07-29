from pathlib import Path
from random import randint
from wordle.models.game import Challenge


class ChallengeGenerator:

    def __init__(self, words_src: str):
        self.words_src = words_src

    def generate_challenge(self) -> Challenge:
        with open(self.words_src, 'r', encoding='UTF-8') as handle:
            words = handle.readlines()
            random_idx = randint(0, len(words) - 1)
            return Challenge(words[random_idx].strip())


def default_generator() -> ChallengeGenerator:
    words_src = Path(__file__)\
        .parent\
        .parent\
        .parent\
        .joinpath('resources/5-letter-words.txt').resolve()
    return ChallengeGenerator(str(words_src))
