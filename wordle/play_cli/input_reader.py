from wordle.errors import IllegalWordLength
from wordle.models.game import Guess
from .interceptors.input_interceptor import InputInterceptor, InputContext
from .errors import QuitGame


class InputReader:

    def accept_guess(self, guess_no: int, guess_count: int) -> Guess:
        pass


class StdInputReader(InputReader):

    def __init__(self, input_interceptor: InputInterceptor):
        self._input_interceptor = input_interceptor

    def accept_guess(self, guess_no: int, guess_count: int) -> Guess:
        while True:
            try:
                raw_guess = input(f'Guess {guess_no + 1}/{guess_count}: ')
                if not self._input_interceptor.intercept_input(InputContext.GUESS_LOOP, raw_guess):
                    return Guess(raw_guess.lower())
            except IllegalWordLength:
                print('Your guess must contain exactly 5 letters')
            except KeyboardInterrupt:
                raise QuitGame
