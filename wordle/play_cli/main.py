from wordle.game.dictionary import load_default_dictionary
from wordle.game.generator import ChallengeGenerator
from wordle.game.challenge import create_instance
from .game_loop import create_game
from .errors import QuitGame


def main():
    dictionary = load_default_dictionary()
    generator = ChallengeGenerator(dictionary)
    challenge = generator.generate_challenge()
    game_loop = create_game(create_instance(challenge))

    try:
        game_loop.run()
    except QuitGame:
        pass


if __name__ == '__main__':
    main()
