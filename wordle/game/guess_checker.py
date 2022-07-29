from wordle.models.game import Challenge, Guess, GuessFeedback, CharFeedback


class GuessChecker:

    def get_feedback(self, challenge: Challenge, guess: Guess) -> GuessFeedback:
        pass


class DefaultGuessChecker(GuessChecker):

    def get_feedback(self, challenge: Challenge, guess: Guess) -> GuessFeedback:
        char_feedbacks: list[CharFeedback] = []
        used_letters = [ c for c in challenge.answer ]
        for i, c in enumerate(guess.guess):
            if c not in used_letters:
                char_feedbacks.append(CharFeedback.NOT_PRESENT)
            else:
                if c != challenge.answer[i]:
                    char_feedbacks.append(CharFeedback.WRONG_POSITION)
                else:
                    char_feedbacks.append(CharFeedback.CORRECT)
                used_letters.remove(c)

        return GuessFeedback(char_feedbacks)
