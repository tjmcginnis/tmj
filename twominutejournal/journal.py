"""journal

A simple library of functions for managing a daily gratitude journal
"""
import datetime

from .errors import EntryAlreadyExistsError


class Journal:
    """Journal packages together all functions needed for journal
    management

    @dependency storage_adapter:
      A Python object that manages persistence (if desired) of the journal
      and entries

      See README for example of a class that adheres to required contract
    """

    def __init__(self, storage_adapter: object):
        """constructor

        @param storage_adapter:
            Adapter to persistence layer used for storing journal entries
        """
        self.storage_adapter = storage_adapter

    def get_todays_prompts(self) -> list:
        """get_todays_prompts
        Check that entry has not already been written today, and if not
        return list of prompts

        @raises EntryAlreadyExistsError:
            An entry already exists for today's date

        @returns list
        """
        today = datetime.datetime.today()
        last_entry = self.storage_adapter.get_last_entry()

        # compare latest entry date to today's date
        if last_entry.get('entry_date').date() == today.date():
            raise EntryAlreadyExistsError(
                "An entry has already been written today")

        prompts = self.storage_adapter.get_prompts()

        return prompts
