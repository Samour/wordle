from dataclasses import dataclass, field
from enum import Enum
from wordle.errors import IllegalWordLength


@dataclass(frozen = True)
class Challenge:

    answer: str
    guess_limit: int = field(default = 5)

    def __post_init__(self):
        if len(self.answer) != 5:
            raise IllegalWordLength()


class ChallengeStatus(Enum):

    IN_PROGRESS = 'IN_PROGRESS'
    SOLVED = 'SOLVED'
    FAILED = 'FAILED'


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


class GuessNotAWord:
    pass
