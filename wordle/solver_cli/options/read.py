from typing import Union, Optional, Any
from enum import Enum
from dataclasses import dataclass
import sys
from re import compile
from wordle.tools.chain import Chain
from .options import \
    ChallengeSource, \
    DictionaryChallengeSource, \
    FilterGuessStrategy, \
    FilterStrategyOptions, \
    ProvidedChallengeSource, \
    SolverOptions, \
    StrategyOptions


class TokenType(Enum):

    KEY = 'KEY'
    VALUE = 'VALUE'


@dataclass(frozen=True)
class OptionToken:

    type: TokenType
    value: str


def tokenize_options(raw_options: tuple[str, ...]) -> tuple[OptionToken, ...]:
    key_pattern = compile('--(.+')
    tokenized: list[OptionToken] = []
    for option in raw_options:
        m = key_pattern.match(option)
        if m:
            tokenized.append(OptionToken(type=TokenType.KEY, value=m[1]))
        else:
            tokenized.append(OptionToken(type=TokenType.VALUE, value=option))

    return tuple(tokenized)


def collate_options(options: tuple[OptionToken, ...]) -> dict[str, Union[str, bool]]:
    current_key: Optional[str] = None
    result: dict[str, Union[str, bool]] = {}
    for option in options:
        if option.type == TokenType.KEY:
            current_key = option.value
            result[current_key] = True
        elif current_key is not None:
            result[current_key] = option.value
            current_key = None
    
    return result


def select_strategy(options: dict[str, Union[str, bool]]) -> StrategyOptions:
    strategy_options: dict[Any, FilterGuessStrategy] = {
        'first': FilterGuessStrategy.GUESS_FIRST,
        'random': FilterGuessStrategy.GUESS_RANDOM,
    }

    return FilterStrategyOptions(
        guess_strategy=strategy_options.get(options['guess-strategy'], FilterGuessStrategy.GUESS_RANDOM),
    )


def select_challenge_source(options: dict[str, Union[str, bool]]) -> ChallengeSource:
    challenge = options['challenge']
    if isinstance(challenge, str):
        return ProvidedChallengeSource()
    else:
        return DictionaryChallengeSource()


def construct_options(options: dict[str, Union[str, bool]]) -> SolverOptions:
    return SolverOptions(
        strategy=select_strategy(options),
        challenge_source=select_challenge_source(options),
        output_style='display',
        debug_output=options['debug'] is True,
    )


def read_options() -> SolverOptions:
    return Chain(sys.argv)\
        .apply(lambda x: tuple(x))\
        .apply(tokenize_options)\
        .apply(collate_options)\
        .apply(construct_options)\
        .value
