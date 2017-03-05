"""entry

A plain Python class representing a journal entry's properties
"""
import uuid
import datetime


class Entry:
    """Entry

    A container for the identifying properties of a journal entry
    """

    def __init__(self):
        """Create a new entry containing a key and timestamp property"""
        self.key = str(uuid.uuid4())
        self.timestamp = datetime.datetime.today()
