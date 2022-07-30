class ArgumentError(Exception):
    pass


class IllegalWordLength(ArgumentError):

    def __init__(self):
        super().__init__('Word is incorrect length')


class SolverFailed(Exception):

    def __init__(self, reason: str):
        self.reason = reason
