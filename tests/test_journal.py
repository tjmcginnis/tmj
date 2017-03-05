"""test_journal

Tests for the Journal class of twominutejournal
"""
import unittest
from unittest.mock import MagicMock
import datetime
import uuid

from twominutejournal.journal import Journal
from twominutejournal.errors import EntryAlreadyExistsError
from twominutejournal.entry import Entry

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

    def test_get_todays_prompts_returns_list(self):
        """Test that get_todays_prompts returns a list"""
        self.adapter.get_last_entry = MagicMock(return_value={
            'id': str(uuid.uuid4()),
            'entry_date': datetime.datetime(2017, 2, 28, 18, 12, 32, 34442)
        })

        self.adapter.get_prompts = MagicMock(return_value=[
            {'key': '14e8017e-b9ec-488b-a708-94243a889588',
             'question': 'I am grateful for...',
             'responses_expected': 2},
            {'key': '2818b0ff-d53c-4a99-b3e9-d415f0977931',
             'question': 'What would make today great?',
             'responses_expected': 2}
        ])

        prompts = self.journal.get_todays_prompts()

        assert isinstance(prompts, list)

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
