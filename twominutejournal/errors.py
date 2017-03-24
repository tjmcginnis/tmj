"""
    twominutejournal.errors
    ~~~~~~~~~~~~~~~~~~~~~~~

    Journal-specific errors.
"""


class Error(Exception):
    '''Base Error class.'''
    pass


class EntryAlreadyExistsError(Error):
    '''Raised when prompts are requested but an entry has
    already been stored today.'''

    def __init__(self, message: str):
        super().__init__()
        self.message = message
