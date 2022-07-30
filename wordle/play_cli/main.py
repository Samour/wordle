from wordle.models.game import Challenge
from wordle.game.dictionary import Dictionary, load_default_dictionary
from wordle.game.generator import ChallengeGenerator
from wordle.game.challenge import create_instance
from .interceptors.input_interceptor import \
    InputInterceptor, \
    NoopInputInterceptor, \
    DelegatingPriorityInputInterceptor, \
    InputContext
from .interceptors.answering_interceptor import AnsweringInterceptor
from .game_loop import create_game
from .errors import QuitGame


class MainLoop:

    def __init__(self, dictionary: Dictionary, generator: ChallengeGenerator):
        self._dictionary = dictionary
        self._generator = generator
        self._input_interceptor: InputInterceptor = NoopInputInterceptor()

    def run(self):
        while True:
            self._play_game()
            self._ask_if_play_again()

    def _play_game(self):
        challenge = self._generator.generate_challenge()
        self._initialize_input_interceptor(challenge)
        game_loop = create_game(create_instance(challenge, self._dictionary), self._input_interceptor)

        game_loop.run()

    def _initialize_input_interceptor(self, challenge: Challenge):
        self._input_interceptor = DelegatingPriorityInputInterceptor([
            AnsweringInterceptor(challenge)
        ])

    def _ask_if_play_again(self):
        answer = input('Would you like to play again? (yes or no): ')
        while True:
            if self._input_interceptor.intercept_input(InputContext.PLAY_AGAIN, answer):
                answer = input('Would you like to play again? (yes or no): ')
            elif answer.lower() == 'yes':
                return
            elif answer.lower() == 'no':
                raise QuitGame()
            else:
                answer = input(f'Cannot understand "{answer}". Please enter yes or no: ')


def main():
    dictionary = load_default_dictionary()
    generator = ChallengeGenerator(dictionary)
    main_loop = MainLoop(dictionary, generator)

    try:
        main_loop.run()
    except QuitGame:
        pass


if __name__ == '__main__':
    main()
