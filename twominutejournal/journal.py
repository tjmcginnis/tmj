"""
    twominutejournal.journal
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A daily gratitude journal library.
"""
import uuid
import datetime

from .errors import EntryAlreadyExistsError


def create_prompt(question: str, responses: int) -> dict:
    '''Create a new journal prompt.'''
    if not isinstance(question, str):
        raise TypeError('question must be of type str')

    if not isinstance(responses, int):
        raise TypeError('responses must be of type int')

    return {
        'question': question,
        'responses': responses
    }


def save_prompt(prompt: dict, storage_adapter: object):
    '''Save a journal prompt.'''
    if not isinstance(prompt, dict):
        raise TypeError('prompt must be of type dict')

    storage_adapter.store_prompt(prompt)


def get_todays_prompts(storage_adapter: object) -> list:
    '''Get today's journal prompts.'''
    today = datetime.datetime.today()
    last_entry = storage_adapter.get_last_entry()

    # compare latest entry date to today's date
    if last_entry.get('entry_date').date() == today.date():
        raise EntryAlreadyExistsError(
            'An entry has already been written today')

    prompts = storage_adapter.get_prompts()

    return prompts


def create_entry() -> dict:
    '''Create a new journal entry.'''
    return {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.today()
    }


def view_all_entries(storage_adapter: object) -> list:
    '''View all journal entries.'''
    return storage_adapter.get_all_entries()


def create_response(prompt_id: str, response_body: str) -> dict:
    '''Create a new journal response.'''
    if not isinstance(prompt_id, str):
        raise TypeError('prompt_id must be of type str.')

    if not isinstance(response_body, str):
        raise TypeError('response_body must be of type str.')

    return {
        'id': str(uuid.uuid4()),
        'prompt_id': prompt_id,
        'response_body': response_body
    }


def submit_responses(entry: dict, responses: list, storage_adapter: object):
    '''Submit an entry and list of responses.'''
    if not isinstance(entry, dict):
        raise TypeError('entry must be of type dict')

    if not isinstance(responses, list):
        raise TypeError('responses must be of type list')

    storage_adapter.store_entry(entry)

    for response in responses:
        storage_adapter.store_response(response, entry['id'])


def view_entry_responses(entry_id: str, storage_adapter: object) -> list:
    '''View the responses for a journal entry.'''
    if not isinstance(entry_id, str):
        raise TypeError('entry_id must be of type str')

    responses = storage_adapter.get_entry_responses(entry_id)

    return responses
