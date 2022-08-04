from wordle.errors import ArgumentError
from wordle.game_api.challenge import ChallengeProvider
from wordle.game_api.dictionary import Dictionary
from wordle.pattern_solver.solver import Solver
from wordle.pattern_solver.filter.guess_selector import GuessSelector, GuessFirstSelector, GuessRandomSelector
from wordle.pattern_solver.filter.solver import FilterSolver
from wordle.pattern_solver.solution_constraints import SolutionConstraints
from wordle.solver_cli.options.options import StrategyOptions, FilterStrategyOptions


def select_guess_strategy(guess_strategy: str) -> GuessSelector:
    if guess_strategy == 'GuessFirstSelector':
        return GuessFirstSelector()
    elif guess_strategy == 'GuessRandomSelector':
        return GuessRandomSelector()
    else:
        raise ArgumentError(f'Unknown guess_strategy for FilterSolver: {guess_strategy}')


def create_filter_solver(
        options: FilterStrategyOptions,
        challenge: ChallengeProvider,
        dictionary: Dictionary) -> Solver:
    return FilterSolver(
        challenge=challenge,
        dictionary=dictionary,
        solution_constraints=SolutionConstraints(),
        guess_selector=select_guess_strategy(options.guess_strategy)
    )


def create_solver(
        options: StrategyOptions,
        challenge: ChallengeProvider,
        dictionary: Dictionary) -> Solver:
    # FilterStrategyOptions is currently the only type
    return create_filter_solver(options, challenge, dictionary)
