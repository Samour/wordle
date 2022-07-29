from wordle.game.generator import default_generator
from wordle.game.challenge import create_instance
from .game_loop import create_game
from .errors import QuitGame


def main():
    generator = default_generator()
    challenge = generator.generate_challenge()
    game_loop = create_game(create_instance(challenge))

    try:
        game_loop.run()
    except QuitGame:
        pass


if __name__ == '__main__':
    main()
