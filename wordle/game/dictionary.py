from pathlib import Path
from wordle.game_api.dictionary import Dictionary


class BinarySearchDictionary(Dictionary):

    def __init__(self, words: list[str]):
        self.words = sorted(words)

    def contains_word(self, word: str) -> bool:
        # Binary search
        lower_bound = 0
        upper_bound = len(self.words) - 1
        while lower_bound + 1 < upper_bound:
            idx = (lower_bound + upper_bound) // 2
            if self.words[idx] < word:
                lower_bound = idx
            elif self.words[idx] > word:
                upper_bound = idx
            else:
                return True
        
        return self.words[lower_bound] == word or self.words[upper_bound] == word


def load_from_file(fname: str) -> Dictionary:
    with open(fname, 'r', encoding='UTF-8') as handle:
        words = handle.readlines()
        return BinarySearchDictionary([ w.strip() for w in words ])


def load_default_dictionary() -> Dictionary:
    default_dictionary_file = Path(__file__)\
        .parent\
        .parent\
        .parent\
        .joinpath('resources/5-letter-words.txt').resolve()
    return load_from_file(str(default_dictionary_file))
