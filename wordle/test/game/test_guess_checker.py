from unittest import TestCase
from wordle.game.guess_checker import DefaultGuessChecker
from wordle.models.game import Challenge, Guess, GuessFeedback, CharFeedback


CHALLENGE = Challenge('abcde')
CHALLENGE_WITH_REPEATED = Challenge('hodor')


class TestDefaultGuessChecker(TestCase):

    def setUp(self):
        self.under_test = DefaultGuessChecker()

    def test_word_fully_correct(self):
        result = self.under_test.get_feedback(CHALLENGE, Guess('abcde'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.CORRECT ] * 5))
    
    def test_word_fully_rearranged(self):
        result = self.under_test.get_feedback(CHALLENGE, Guess('eabcd'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.WRONG_POSITION ] * 5))

    def test_word_fully_wrong(self):
        result = self.under_test.get_feedback(CHALLENGE, Guess('vwxyz'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.NOT_PRESENT ] * 5))

    def test_word_mixed(self):
        result = self.under_test.get_feedback(CHALLENGE, Guess('cbaxy'))

        self.assertEqual(result, GuessFeedback([
            CharFeedback.WRONG_POSITION,
            CharFeedback.CORRECT,
            CharFeedback.WRONG_POSITION,
            CharFeedback.NOT_PRESENT,
            CharFeedback.NOT_PRESENT,
        ]))

    def test_word_overused_letter(self):
        result = self.under_test.get_feedback(CHALLENGE, Guess('abcda'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.CORRECT ] * 4 + [ CharFeedback.NOT_PRESENT ]))

    def test_word_repeated_letters_fully_correct(self):
        result = self.under_test.get_feedback(CHALLENGE_WITH_REPEATED, Guess('hodor'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.CORRECT ] * 5))
    
    def test_word_repeated_letters_fully_rearranged(self):
        result = self.under_test.get_feedback(CHALLENGE_WITH_REPEATED, Guess('dhoro'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.WRONG_POSITION ] * 5))

    def test_word_repeated_letters_fully_wrong(self):
        result = self.under_test.get_feedback(CHALLENGE_WITH_REPEATED, Guess('vwxyz'))

        self.assertEqual(result, GuessFeedback([ CharFeedback.NOT_PRESENT ] * 5))

    def test_word_repeated_letters_mixed(self):
        result = self.under_test.get_feedback(CHALLENGE_WITH_REPEATED, Guess('rodeo'))

        self.assertEqual(result, GuessFeedback([
            CharFeedback.WRONG_POSITION,
            CharFeedback.CORRECT,
            CharFeedback.CORRECT,
            CharFeedback.NOT_PRESENT,
            CharFeedback.WRONG_POSITION,
        ]))
