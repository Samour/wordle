from dataclasses import dataclass
from .game import Guess


@dataclass(frozen=True)
class Solution:

    guesses: list[Guess]
    solution_found: bool
