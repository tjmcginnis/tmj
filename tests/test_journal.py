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
