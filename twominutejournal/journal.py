"""journal

A simple library of functions for managing a daily gratitude journal
"""


class Journal:
    """Journal packages together all functions needed for journal
    management

    @dependency storage_adapter:
      A Python object that manages persistence (if desired) of the journal
      and entries

      See README for example of a class that adheres to required contract
    """

    def __init__(self, storage_adapter):
        """constructor

        @param storage_adapter:
            Adapter to persistence layer used for storing journal entries
        """
        self.storage_adapter = storage_adapter

    def get_todays_prompts(self):
        """get_todays_prompts

        @raises EntryAlreadyExistsError:
            An entry already exists for today's date
        """
        last = self.storage_adapter.get_last_entry()

        return list()
