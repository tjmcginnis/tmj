"""errors

Journal specific errors and exceptions
"""

class Error(Exception):
    """Base class for journal exceptions"""
    pass


class EntryAlreadyExistsError(Error):
    """Raised when prompts are requested but an entry has already been
    written today

    @param message: a message explaining the error
    """

    def __init__(self, message):
        super().__init__()
        self.message = message
