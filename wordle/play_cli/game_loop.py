from wordle.models.game import ChallengeStatus, GuessNotAWord
from wordle.game.challenge import ChallengeInstance
from .interceptors.input_interceptor import InputInterceptor
from .input_reader import InputReader, StdInputReader
from .output_renderer import OutputRenderer, StdOutputRenderer


class GameLoop:

    def __init__(self, challenge: ChallengeInstance, input_reader: InputReader, output_renderer: OutputRenderer):
        self._challenge = challenge
        self._input_reader = input_reader
        self._output_renderer = output_renderer

    def run(self) -> None:
        while self._challenge.challenge_status == ChallengeStatus.IN_PROGRESS:
            guess = self._input_reader.accept_guess(
                len(self._challenge.guesses),
                self._challenge.challenge.guess_limit,
            )
            feedback = self._challenge.make_guess(guess)

            if isinstance(feedback, GuessNotAWord):
                self._output_renderer.print_guess_not_a_word(guess)
            else:
                self._output_renderer.print_guess_feedback(guess, feedback)

        if self._challenge.challenge_status == ChallengeStatus.SOLVED:
            self._output_renderer.print_winner_message()
        else:
            self._output_renderer.print_loser_message()


def create_game(challenge: ChallengeInstance, input_interceptor: InputInterceptor) -> GameLoop:
    return GameLoop(challenge, StdInputReader(input_interceptor), StdOutputRenderer())
