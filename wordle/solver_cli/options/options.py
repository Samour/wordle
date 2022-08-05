from typing import Union
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class FilterStrategyOptions:

    guess_strategy: str


StrategyOptions = FilterStrategyOptions


class DictionaryChallengeSource:
    pass


class ProvidedChallengeSource:
    pass


ChallengeSource = Union[DictionaryChallengeSource, ProvidedChallengeSource]


@dataclass(frozen=True)
class SolverOptions:

    strategy: StrategyOptions
    challenge_source: ChallengeSource
    output_style: str
    debug_output: bool
