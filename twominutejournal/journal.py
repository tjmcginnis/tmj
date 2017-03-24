"""
    twominutejournal.journal
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A daily gratitude journal library.
"""
import datetime

from .entry import Entry
from .response import Response
from .errors import EntryAlreadyExistsError


def create_prompt(question: str, responses_expected: int) -> dict:
    '''Create a new journal prompt.'''
    if not isinstance(question, str):
        raise TypeError('prompt question must be a str')

    if not isinstance(responses_expected, int):
        raise TypeError('prompt responses expected must be an int')

    return {
        'question': question,
        'responses_expected': responses_expected
    }


def save_prompt(prompt: dict, storage_adapter: object):
    '''Save a journal prompt.'''
    if not isinstance(prompt, dict):
        raise TypeError('prompt must be a dict')

    storage_adapter.store_prompt(prompt)


def get_todays_prompts(storage_adapter: object) -> list:
    '''Get today's journal prompts.'''
    today = datetime.datetime.today()
    last_entry = storage_adapter.get_last_entry()

    # compare latest entry date to today's date
    if last_entry.get('entry_date').date() == today.date():
        raise EntryAlreadyExistsError(
            "An entry has already been written today")

    prompts = storage_adapter.get_prompts()

    return prompts


def create_entry() -> dict:
    '''Create a new journal entry.'''
    return Entry().__dict__


def view_all_entries(storage_adapter: object) -> list:
    '''View all journal entries.'''
    return storage_adapter.get_all_entries()


def create_response(prompt_key: str, response_body: str) -> dict:
    '''Create a new journal response.'''
    try:
        return Response(prompt_key, response_body).__dict__
    except TypeError:
        raise


def submit_responses(entry: dict, responses: list, storage_adapter: object):
    '''Submit an entry and list of responses.'''
    if not isinstance(entry, dict):
        raise TypeError("entry must be of type dict")

    if not isinstance(responses, list):
        raise TypeError("responses must be of type list")

    storage_adapter.store_entry(entry)

    for response in responses:
        storage_adapter.store_response(response, entry['key'])


def view_entry_responses(entry_key: str, storage_adapter: object) -> list:
    '''View the responses for a journal entry.'''
    if not isinstance(entry_key, str):
        raise TypeError("entry_key must be of type str")

    responses = storage_adapter.get_entry_responses(entry_key)

    return responses
