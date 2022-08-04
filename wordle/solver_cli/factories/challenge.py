from wordle.models.game import Challenge
from wordle.game_api.challenge import ChallengeProvider
from wordle.game_api.dictionary import Dictionary
from wordle.game.generator import ChallengeGenerator
from wordle.game.challenge import create_instance
from wordle.solver_cli.options.options import ChallengeSource, DictionaryChallengeSource


class ChallengeFactory:

    def __init__(self, source: ChallengeSource, dictionary: Dictionary, generator: ChallengeGenerator):
        self._source = source
        self._dictionary = dictionary
        self._generator = generator

    def create_challenge(self) -> ChallengeProvider:
        return create_instance(self._create_challenge_model(), self._dictionary)

    def _create_challenge_model(self) -> Challenge:
        if isinstance(self._source, DictionaryChallengeSource):
            return self._generator.generate_challenge()
        else:
            return Challenge(self._source.answer)


def create_factory(source: ChallengeSource, dictionary: Dictionary) -> ChallengeFactory:
    return ChallengeFactory(source, dictionary, ChallengeGenerator(dictionary))
