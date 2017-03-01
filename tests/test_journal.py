"""journal_test

Tests for the Journal class of twominutejournal
"""
import unittest
from unittest import mock
import datetime

from twominutejournal import journal


class MockStorageAdapter:
    """Mock storage adapter class for testing purposes

    Functions requiring return data just return dummy data
    """

    def store_entry(self, entry):
        """Mock store_entry

        Does not need to return anything
        """
        pass

    def store_response(self, response):
        """Mock store_response

        Does not need to return anything
        """
        pass

    def get_all_entries(self):
        """Mock get_all_entries

        Return empty list
        """
        return list()

    def get_entry_responses(self, entry_id):
        """Mock get_entry_responses

        Return empty list
        """
        return list()

    def get_last_entry(self):
        """Mock get_last_entry

        Return a dict representing a mock entry
        """
        date = datetime.datetime(2017, 2, 28, 12, 10, 45)
        return {
            'id': 'abcd1234-ab12-1234-b2c1-b5328c1322bf',
            'date': str(date)}

    def get_prompts(self):
        """Mock get_prompts

        Return list containing two dicts, representing the current prompts
        """
        return [
            {
                'id': '14e8017e-b9ec-488b-a708-94243a889588',
                'Question': 'I am grateful for...',
                'ResponsesExpected': 2
            },
            {
                'id': '2818b0ff-d53c-4a99-b3e9-d415f0977931',
                'Question': 'What would make today great?',
                'ResponsesExpected': 2
            }
        ]


class TestJournal(unittest.TestCase):
    """Tests for Journal functions"""

    def setUp(self):
        """Set up a journal instance to use for all tests"""
        adapter = MockStorageAdapter()
        self.journal = journal.Journal(adapter)

    def test_journal_has_storage_adapter(self):
        """Test that the storage adapter was properly associated with the
        Journal instance
        """
        assert self.journal.storage_adapter is not None

    def test_get_todays_prompts_returns_list(self):
        """Test that get_todays_prompts returns a list if last entry
        was not created today
        """
        mock_date = datetime.datetime(2017, 3, 1, 11, 18, 32)
        datetime.now = mock.MagicMock(return_value=mock_date)
        prompts = self.journal.get_todays_prompts()
        assert isinstance(prompts, list)
