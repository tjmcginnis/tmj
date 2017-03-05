"""journal

A simple library of functions for managing a daily gratitude journal
"""
import datetime

from .entry import Entry
from .response import Response
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

    def create_entry(self) -> dict:
        """create_entry

        Create a dictionary representing a journal entry, containing
        a uuid4 generated id and datetime object representing today's
        date

        @returns dict
        """
        return Entry().__dict__

    def view_all_entries(self) -> list:
        """view_all_entries

        Return a list of all stored journal entries

        @returns list
        """
        return self.storage_adapter.get_all_entries()

    def create_response(self, prompt_key: str, response_body: str) -> dict:
        """create_response

        Create a dictionary representing a new journal response,
        containing a uuid4 generated key, string representing a
        prompt_key, and string representing the response body

        @returns dict
        """
        return Response(prompt_key, response_body).__dict__
