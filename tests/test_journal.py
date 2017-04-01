"""
    tests.test_journal
    ~~~~~~~~~~~~~~~~~~

    Unit tests for twominutejournal.journal.
"""
import unittest
from unittest.mock import MagicMock
import datetime
import uuid

from twominutejournal import journal
from twominutejournal.errors import EntryAlreadyExistsError
from .adapter import MockStorageAdapter


class TestJournal(unittest.TestCase):
    '''TestJournal'''

    def setUp(self):
        '''Instantiate a mock storage adapter for the test suite.'''
        self.adapter = MockStorageAdapter()

    def test_get_todays_prompts_calls_get_prompts(self):
        '''journal.get_todays_prompts calls correct storage
        adapter method.
        '''
        self.adapter.get_last_entry = MagicMock(return_value={
            'id': str(uuid.uuid4()),
            'entry_date': datetime.datetime(2017, 2, 28, 18, 12, 32, 34442)
        })

        self.adapter.get_prompts = MagicMock(return_value=list())
        journal.get_todays_prompts(self.adapter)
        assert self.adapter.get_prompts.call_count == 1

    def test_get_todays_prompts_raises_error(self):
        '''journal.get_todays_prompts raises EntryAlreadyExistsError
        if the date of the stored entry is today's date.
        '''
        self.adapter.get_last_entry = MagicMock(return_value={
            'id': str(uuid.uuid4()),
            'entry_date': datetime.datetime.today()
        })

        with self.assertRaises(EntryAlreadyExistsError):
            journal.get_todays_prompts(self.adapter)

    def test_create_entry_returns_with_dict(self):
        '''journal.create_entry returns a dict with correct
        properties.
        '''
        entry = journal.create_entry()

        assert isinstance(entry, dict)
        assert isinstance(entry['id'], str)
        assert isinstance(entry['timestamp'], datetime.datetime)

    def test_view_all_entries_calls_get_all_entries(self):
        '''journal.view_all_entries calls the correct storage
        adapter method.
        '''
        self.adapter.get_all_entries = MagicMock(return_value=list())
        journal.view_all_entries(self.adapter)
        assert self.adapter.get_all_entries.call_count == 1

    def test_create_response_returns_with_dict(self):
        '''journal.create_response returns a dict with correct
        properties.
        '''
        prompt_id = '14e8017e-b9ec-488b-a708-94243a889588'
        response_body = 'My hilarious dogs.'

        response = journal.create_response(
            prompt=prompt_id,
            body=response_body)

        assert isinstance(response, dict)
        assert isinstance(response['id'], str)
        assert response['prompt'] == prompt_id
        assert response['body'] == response_body

    def test_create_response_raises_type_error(self):
        '''journal.create_response raises TypeError if passed incorrectly
        typed argument
        '''
        with self.assertRaises(TypeError):
            journal.create_response(
                prompt=12345,
                body='Doesn\'t matter')

        with self.assertRaises(TypeError):
            journal.create_response(
                prompt='Prompt id',
                body=2)

    def test_submit_responses_calls_store_entry(self):
        '''journal.submit_responses calls the correct storage
        adapter method.
        '''
        self.adapter.store_entry = MagicMock(return_value=None)
        journal.submit_responses(dict(), list(), self.adapter)
        assert self.adapter.store_entry.call_count == 1

    def test_submit_responses_calls_store_response(self):
        '''journal.submit_responses calls the correct storage
        adapter method.
        '''
        entry_id = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'
        self.adapter.store_response = MagicMock(return_value=None)

        response = {
            'prompt': '14e8017e-b9ec-488b-a708-94243a889588',
            'body': 'My hilarious dogs.'
        }

        journal.submit_responses({'id': entry_id}, [response],
                                 self.adapter)
        assert self.adapter.store_response.call_count == 1

    def test_submit_responses_raises_type_error(self):
        '''journal.submit_responses raises TypeError if passed
        incorrectly typed argument.
        '''
        with self.assertRaises(TypeError):
            journal.submit_responses("Entry", list(), self.adapter)

        with self.assertRaises(TypeError):
            journal.submit_responses(dict(), 'responses', self.adapter)

    def test_view_entry_responses_calls_get_entry_responses(self):
        '''journal.view_entry_responses calls correct storage adapter
        method.'''
        entry_id = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'
        self.adapter.get_entry_responses = MagicMock(return_value=list())

        journal.view_entry_responses(entry_id, self.adapter)
        assert self.adapter.get_entry_responses.call_count == 1

    def test_view_entry_responses_raises_type_error(self):
        '''journal.view_entry_responses raises TypeError if argument
        is not str.
        '''
        with self.assertRaises(TypeError):
            journal.view_entry_responses(1234, self.adapter)

    def test_create_prompt_returns_with_dict(self):
        '''journal.create_prompt returns a dict with correct
        properties.
        '''
        question = 'I am grateful for...'
        num_responses = 2

        prompt = journal.create_prompt(
            question=question,
            responses=num_responses)

        assert isinstance(prompt, dict)
        assert prompt['question'] == question
        assert prompt['responses'] == num_responses

    def test_create_prompt_raises_type_error(self):
        '''journal.create_prompt raises TypeError if passed
        incorrectly typed arguments.'''
        with self.assertRaises(TypeError):
            journal.create_prompt(6, 2)

        with self.assertRaises(TypeError):
            journal.create_prompt('Question', 'Responses Expected')

    def test_save_prompt_calls_store_prompt(self):
        '''journal.add_prompt calls correct storage adapter
        method.
        '''
        prompt = dict()
        self.adapter.store_prompt = MagicMock(return_value=None)

        journal.save_prompt(prompt, self.adapter)
        assert self.adapter.store_prompt.call_count == 1

    def test_save_prompt_raises_type_error(self):
        '''journal.save_prompt raises TypeError if passed
        incorrect argument type.'''
        with self.assertRaises(TypeError):
            journal.save_prompt(list(), self.adapter)
