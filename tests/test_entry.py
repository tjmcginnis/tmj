"""test_entry

Tests for the Entry class of twominutejournal
"""
import unittest
import datetime

from twominutejournal.entry import Entry


class TestEntry(unittest.TestCase):
    """Tests for Entry"""

    def setUp(self):
        """Create an Entry instance for test suite"""
        self.entry = Entry()

    def test_constructor_returns_with_valid_key(self):
        """Test that when a new Entry object is instantiated the key
        propert contains a 36 character string
        """

        assert isinstance(self.entry.key, str)
        assert len(self.entry.key) == 36

    def test_constructor_returns_with_valid_date(self):
        """Test that when a new Entry object is instantiated the timestamp
        containers a datetime object representing the current date
        """

        assert isinstance(self.entry.timestamp, datetime.datetime)
        assert self.entry.timestamp.date() == datetime.datetime.today().date()
