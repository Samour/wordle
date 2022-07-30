import re
from typing import Union
from dataclasses import dataclass
from wordle.models.game import Guess, GuessFeedback, CharFeedback, WORD_LENGTH


@dataclass(frozen=True)
class CharacterKnown:

    character: str


@dataclass(frozen=True)
class EliminatedCharacters:

    characters: frozenset[str]

    def with_additional(self, additional: set[str]):
        return EliminatedCharacters(self.characters.union(additional))


ConstraintDescriptor = Union[CharacterKnown, EliminatedCharacters]


class SolutionConstraints:

    def __init__(self):
        self.required_characters: set[str] = set()
        self.positional_constraints: list[ConstraintDescriptor] = [ EliminatedCharacters() ] * WORD_LENGTH

    def push_feedback(self, guess: Guess, feedback: GuessFeedback) -> None:
        not_present: set[str] = set()
        for i, c in enumerate(guess.guess):
            current_descriptor = self.positional_constraints[i]
            if isinstance(current_descriptor, CharacterKnown):
                continue

            if feedback.feedback[i] == CharFeedback.CORRECT:
                self.required_characters.add(c)
                self.positional_constraints[i] = CharacterKnown(c)
            elif feedback.feedback[i] == CharFeedback.WRONG_POSITION:
                self.required_characters.add(c)
                self.positional_constraints = current_descriptor.with_additional({c})
            elif feedback.feedback[i] == CharFeedback.NOT_PRESENT:
                not_present.add(c)
        
        if len(not_present) > 0:
            for i, constraint in enumerate(self.positional_constraints):
                if isinstance(constraint, EliminatedCharacters):
                    self.positional_constraints[i] = constraint.with_additional(not_present)

    def produce_char_pattern(self, i: int) -> str:
        constraint = self.positional_constraints[i]
        if isinstance(constraint, CharacterKnown):
            return constraint.character
        elif len(constraint.characters) > 0:
            return '[^{}]'.format(
                ''.join(constraint.characters)
            )
        else:
            return '.'

    def produce_patterns(self) -> list[re.Pattern]:
        patterns: list[re.Pattern] = []
        known_without_position = self.required_characters.difference(
            { c.character for c in self.positional_constraints if isinstance(c, CharacterKnown) }
        )
        for c in known_without_position:
            patterns.append(re.compile(c))
        
        patterns.append(re.compile(
            ''.join(
                [ self.produce_char_pattern(i) for i in range(len(self.positional_constraints)) ]
            )
        ))

        return patterns
