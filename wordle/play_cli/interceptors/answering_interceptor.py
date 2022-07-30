from wordle.models.game import Challenge
from .input_interceptor import InputContext, InputInterceptor


class AnsweringInterceptor(InputInterceptor):

    def __init__(self, challenge: Challenge):
        self._challenge = challenge

    def intercept_input(self, context: InputContext, input: str) -> bool:
        if self._do_intercept(context, input.lower()):
            print(f'The answer to this wordle is: {self._challenge.answer}')
            return True
        else:
            return False

    def _do_intercept(self, context: InputContext, input: str) -> bool:
        if context == InputContext.PLAY_AGAIN:
            return input == '/answer'
        elif context == InputContext.GUESS_LOOP:
            return input == '/cheat'
        else:
            return False
