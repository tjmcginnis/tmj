"""journal_test

Tests for the Journal class of twominutejournal
"""
import unittest
from unittest.mock import MagicMock
import datetime

from twominutejournal import journal, errors


class MockStorageAdapter:
    """Mock storage adapter class.

    Will be patched for testing purposes
    """

    def store_entry(self, entry):
        """Mock store_entry"""
        pass

    def store_response(self, response):
        """Mock store_response"""
        pass

    def get_all_entries(self):
        """Mock get_all_entries"""
        pass

    def get_entry_responses(self, entry_id):
        """Mock get_entry_responses"""
        pass

    def get_last_entry(self):
        """Mock get_last_entry"""
        pass

    def get_prompts(self):
        """Mock get_prompts"""
        pass


class TestJournal(unittest.TestCase):
    """Tests for Journal methods"""

    def setUp(self):
        """Set up a journal instance to use for all tests"""
        self.adapter = MockStorageAdapter()
        self.journal = journal.Journal(self.adapter)

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
            'id': '0385f421-a980-4b03-9b88-ee67af63c90d',
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
            'id': '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
            'entry_date': datetime.datetime.today()
        })

        with self.assertRaises(errors.EntryAlreadyExistsError):
            self.journal.get_todays_prompts()
