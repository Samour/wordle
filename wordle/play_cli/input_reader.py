from wordle.errors import IllegalWordLength
from wordle.models.game import Guess
from .errors import QuitGame


class InputReader:

    def accept_guess(self, guess_no: int, guess_count: int) -> Guess:
        pass


class StdInputReader(InputReader):

    def accept_guess(self, guess_no: int, guess_count: int) -> Guess:
        while True:
            try:
                raw_guess = input(f'Guess {guess_no + 1}/{guess_count}: ').lower()
                return Guess(raw_guess)
            except IllegalWordLength:
                print('Your guess must contain exactly 5 letters')
            except KeyboardInterrupt:
                raise QuitGame
