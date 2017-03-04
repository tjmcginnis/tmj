"""test_journal

Tests for the Journal class of twominutejournal
"""
import unittest
from unittest.mock import MagicMock
import datetime
import uuid

from .adapter import MockStorageAdapter

from twominutejournal import journal, errors


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

        with self.assertRaises(errors.EntryAlreadyExistsError):
            self.journal.get_todays_prompts()

    def test_create_entry_returns_with_valid_id(self):
        """Test that create_entry returns a dict with an id property
        that is a 36 character string
        """
        entry = self.journal.create_entry()

        assert isinstance(entry['id'], str)
        assert len(entry['id']) == 36

    def test_create_entry_returns_with_valid_date(self):
        """Test that create_entry returns a dict with a date property
        that is a datetime object representing the current date
        """
        entry = self.journal.create_entry()

        assert entry['date'].date() == datetime.datetime.today().date()
