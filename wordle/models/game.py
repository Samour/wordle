from dataclasses import dataclass
from enum import Enum
from wordle.errors import IllegalWordLength


@dataclass(frozen = True)
class Challenge:

    answer: str

    def __post_init__(self):
        if len(self.answer) != 5:
            raise IllegalWordLength()


@dataclass(frozen = True)
class Guess:

    guess: str

    def __post_init__(self):
        if len(self.guess) != 5:
            raise IllegalWordLength()


class CharFeedback(Enum):

    NOT_PRESENT = 'NOT_PRESENT'
    WRONG_POSITION = 'WRONG_POSITION'
    CORRECT = 'CORRECT'


@dataclass(frozen = True)
class GuessFeedback:

    feedback: list[CharFeedback]

    def __post_init__(self):
        if len(self.feedback) != 5:
            raise IllegalWordLength()
