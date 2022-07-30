from wordle.models.game import Guess, GuessFeedback, CharFeedback


class OutputRenderer:

    def print_guess_feedback(self, guess: Guess, feedback: GuessFeedback) -> None:
        pass

    def print_guess_not_a_word(self, guess: Guess):
        pass

    def print_winner_message(self) -> None:
        pass

    def print_loser_message(self) -> None:
        pass


_COLOUR_CORRECT = '\033[92m'
_COLOUR_WRONG_POSITION = '\033[93m'
_COLOUR_WRONG = '\033[0m'
_COLOUR_FAILED = '\033[91m'
_COLOUR_RESET = '\033[0m'


class StdOutputRenderer(OutputRenderer):

    def print_guess_feedback(self, guess: Guess, feedback: GuessFeedback) -> None:
        line_parts: list[str] = []
        
        for i, c in enumerate(guess.guess):
            if feedback.feedback[i] == CharFeedback.CORRECT:
                line_parts.append(_COLOUR_CORRECT)
            elif feedback.feedback[i] == CharFeedback.WRONG_POSITION:
                line_parts.append(_COLOUR_WRONG_POSITION)
            else:
                line_parts.append(_COLOUR_WRONG)
            line_parts.append(c)
        
        line_parts.append(_COLOUR_RESET)
        print(''.join(line_parts))

    def print_guess_not_a_word(self, guess: Guess):
        print(f'{guess.guess} is not a word')

    def print_winner_message(self) -> None:
        print(f'{_COLOUR_CORRECT}Congratulations! You solved the wordle{_COLOUR_RESET}')

    def print_loser_message(self) -> None:
        print(f'{_COLOUR_FAILED}Too bad! No more guesses{_COLOUR_RESET}')
