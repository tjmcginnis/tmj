"""test_journal

Tests for the Journal class of twominutejournal
"""
import unittest
from unittest.mock import MagicMock
import datetime
import uuid

from twominutejournal.journal import Journal
from twominutejournal.errors import EntryAlreadyExistsError

from .adapter import MockStorageAdapter


class TestJournal(unittest.TestCase):
    """Tests for Journal methods"""

    def setUp(self):
        """Set up a journal instance to use for all tests"""
        self.adapter = MockStorageAdapter()
        self.journal = Journal(self.adapter)

    def test_journal_has_storage_adapter(self):
        """Test that the storage adapter was properly associated with the
        Journal instance
        """
        assert self.journal.storage_adapter is not None

    def test_get_todays_prompts_calls_get_prompts(self):
        """Test that get_todays_prompts calls the get_prompts method
        of the storage adapter
        """
        self.adapter.get_last_entry = MagicMock(return_value={
            'id': str(uuid.uuid4()),
            'entry_date': datetime.datetime(2017, 2, 28, 18, 12, 32, 34442)
        })

        self.adapter.get_prompts = MagicMock(return_value=list())

        self.journal.get_todays_prompts()

        self.adapter.get_prompts.assert_called_once()

    def test_get_todays_prompts_raises_error(self):
        """Test that get_todays_prompts raises EntryAlreadyExistsError
        when the date of the last stored entry is the same as today's date
        """
        self.adapter.get_last_entry = MagicMock(return_value={
            'id': str(uuid.uuid4()),
            'entry_date': datetime.datetime.today()
        })

        with self.assertRaises(EntryAlreadyExistsError):
            self.journal.get_todays_prompts()

    def test_create_entry_returns_with_dict(self):
        """Test that create_entry returns a dictionary"""
        entry = self.journal.create_entry()

        assert isinstance(entry, dict)

    def test_create_entry_returns_with_correct_properties(self):
        """Test that create_entry returns a dict with key and timestamp
        properties
        """
        entry = self.journal.create_entry()

        assert entry['key'] is not None
        assert entry['timestamp'] is not None

    def test_view_all_entries_calls_get_all_entries(self):
        """Test that view_all_entries calls the get_all_entries method
        of the storage adapter
        """
        self.adapter.get_all_entries = MagicMock(return_value=list())

        self.journal.view_all_entries()

        self.adapter.get_all_entries.assert_called_once()

    def test_create_response_returns_with_dict(self):
        """Test that create_response returns a dictionary"""
        response = self.journal.create_response(
            prompt_key='14e8017e-b9ec-488b-a708-94243a889588',
            response_body='My hilarious dogs.')

        assert isinstance(response, dict)

    def test_create_response_returns_with_correct_properties(self):
        """Test that create_response returns a dict with key, prompt_key,
        and response_body properties
        """
        response = self.journal.create_response(
            prompt_key='14e8017e-b9ec-488b-a708-94243a889588',
            response_body='My hilarious dogs.')

        assert response['key'] is not None
        assert response['prompt_key'] is not None
        assert response['response_body'] is not None

    def test_create_response_raises_type_error(self):
        """Test that create_response raises a TypeError if error raised
        when initializing response
        """
        with self.assertRaises(TypeError):
            response = self.journal.create_response(
                prompt_key=12345,
                response_body="Doesn't matter")

    def test_submit_responses_calls_store_entry(self):
        """Test that submit_responses calls the store_entry method
        of the storage adapter
        """
        self.adapter.store_entry = MagicMock(return_value=None)

        self.journal.submit_responses(dict(), list())

        self.adapter.store_entry.assert_called_once()

    def test_submit_responses_calls_store_response(self):
        """Test that submit_responses calls the store_response method
        of the storage adapter
        """
        self.adapter.store_response = MagicMock(return_value=None)

        response = {
            'key': '6c1de71f-5e99-4dfc-a418-54817b1c73bb',
            'prompt_key': '14e8017e-b9ec-488b-a708-94243a889588',
            'response_body': 'My hilarious dogs.'
        }

        entry_key = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'

        self.journal.submit_responses({'key': entry_key}, [response])

        self.adapter.store_response.assert_called_with(response, entry_key)

    def test_submit_responses_raises_type_error_entry(self):
        """Test that submit_responses raises a TypeError if entry
        argument is not a dict
        """
        with self.assertRaises(TypeError):
            self.journal.submit_responses("Entry", list())

    def test_submit_responses_raises_type_error_responses(self):
        """Test that submit_responses raises a TypeError if entry
        argument is not a dict
        """
        with self.assertRaises(TypeError):
            self.journal.submit_responses(dict(), "responses")

    def test_view_entry_responses_calls_get_entry_responses(self):
        """Test that view_entry_responses calls the get_entry_responses
        method of the storage adapter
        """
        entry_key = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'

        self.adapter.get_entry_responses = MagicMock(return_value=list())

        self.journal.view_entry_responses(entry_key)

        self.adapter.get_entry_responses.assert_called_with(entry_key)

    def test_view_entry_responses_raises_type_error(self):
        """Test that view_entry_responses raises a TypeError if entry_key
        argument is not a str
        """
        with self.assertRaises(TypeError):
            self.journal.view_entry_responses(1234)
