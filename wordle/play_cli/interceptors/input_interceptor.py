from enum import Enum


class InputContext(Enum):

    PLAY_AGAIN = 'PLAY_AGAIN'
    GUESS_LOOP = 'GUESS_LOOP'


class InputInterceptor:

    def intercept_input(self, context: InputContext, input: str) -> bool:
        pass


class NoopInputInterceptor(InputInterceptor):

    def intercept_input(self, context: InputContext, input: str) -> bool:
        return False


class DelegatingPriorityInputInterceptor(InputInterceptor):

    def __init__(self, delegates: list[InputInterceptor]):
        self._delegates = delegates

    def intercept_input(self, context: InputContext, input: str) -> bool:
        for delegate in self._delegates:
            if delegate.intercept_input(context, input):
                return True

        return False
