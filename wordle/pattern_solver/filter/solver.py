from wordle.errors import SolverFailed
from wordle.models.solution import Solution
from wordle.models.game import ChallengeStatus, Guess, GuessNotAWord
from wordle.game_api.challenge import ChallengeProvider
from wordle.game_api.dictionary import Dictionary
from wordle.pattern_solver.solver import Solver
from wordle.pattern_solver.solution_constraints import SolutionConstraints
from .guess_selector import GuessSelector


class FilterSolver(Solver):

    def __init__(
            self,
            challenge: ChallengeProvider,
            dictionary: Dictionary,
            solution_constraints: SolutionConstraints,
            guess_selector: GuessSelector):
        self.challenge = challenge
        self._dictionary = tuple(dictionary.words)
        self._solution_constraints = solution_constraints
        self._guess_selector = guess_selector

    def solve(self) -> Solution:
        guesses: list[Guess] = []
        while self.challenge.challenge_status == ChallengeStatus.IN_PROGRESS:
            guess = self._select_next_guess()
            feedback = self.challenge.make_guess(guess)

            if isinstance(feedback, GuessNotAWord):
                # This should not be possible
                raise SolverFailed('GuessNotAWord: solver started guessing non-dictionary words')
            guesses.append(guess)
            self._solution_constraints.push_feedback(guess, feedback)

        return Solution(
            guesses=guesses,
            solution_found=self.challenge.challenge_status == ChallengeStatus.SOLVED
        )
    
    def _select_next_guess(self) -> Guess:
        self._reduce_dictionary()

        return self._guess_selector.select_guess(self._dictionary)

    def _reduce_dictionary(self) -> None:
        patterns = self._solution_constraints.produce_patterns()
        def matches(word: str) -> bool:
            for pattern in patterns:
                if not pattern.match(word):
                    return False
            return True

        self._dictionary = tuple(filter(matches, self._dictionary))
