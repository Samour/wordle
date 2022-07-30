from wordle.models.game import Challenge, Guess, GuessFeedback, CharFeedback, WORD_LENGTH


class GuessChecker:

    def get_feedback(self, challenge: Challenge, guess: Guess) -> GuessFeedback:
        pass


class DefaultGuessChecker(GuessChecker):

    def get_feedback(self, challenge: Challenge, guess: Guess) -> GuessFeedback:
        char_feedbacks = [ CharFeedback.NOT_PRESENT ] * WORD_LENGTH
        used_letters = [ c for c in challenge.answer ]
        # Give "priority" to correct letter, correct position guesses
        for i, c in enumerate(guess.guess):
            if c == challenge.answer[i]:
                char_feedbacks[i] = CharFeedback.CORRECT
                used_letters.remove(c)
        for i, c in enumerate(guess.guess):
            if char_feedbacks[i] == CharFeedback.NOT_PRESENT and c in used_letters:
                char_feedbacks[i] = CharFeedback.WRONG_POSITION
                used_letters.remove(c)

        return GuessFeedback(char_feedbacks)
