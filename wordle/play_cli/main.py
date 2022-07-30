from wordle.game.dictionary import Dictionary, load_default_dictionary
from wordle.game.generator import ChallengeGenerator
from wordle.game.challenge import create_instance
from .game_loop import create_game
from .errors import QuitGame


class MainLoop:

    def __init__(self, dictionary: Dictionary, generator: ChallengeGenerator):
        self._dictionary = dictionary
        self._generator = generator

    def run(self):
        while True:
            self._play_game()
            self._ask_if_play_again()

    def _play_game(self):
        challenge = self._generator.generate_challenge()
        game_loop = create_game(create_instance(challenge, self._dictionary))
        game_loop.run()

    def _ask_if_play_again(self):
        answer = input('Would you like to play again? (yes or no): ').lower()
        while True:
            if answer == 'yes':
                return
            elif answer == 'no':
                raise QuitGame()
            answer = input(f'Cannot understand "{answer}". Please enter yes or no: ').lower()


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
