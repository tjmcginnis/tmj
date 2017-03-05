"""test_entry

Tests for the Prompt class of twominutejournal
"""
import unittest

from twominutejournal.prompt import Prompt

QUESTION = 'What would make today great?'
RESPONSES_EXPECTED = 2

class TestPrompt(unittest.TestCase):
    """Tests for Prompt"""

    def setUp(self):
        """Create a prompt instance for test suite"""
        self.prompt = Prompt(QUESTION, RESPONSES_EXPECTED)

    def test_constructor_returns_with_valid_key(self):
        """Test that when a new Prompt object is instantiated the key
        property contains a 36 character string
        """
        assert isinstance(self.prompt.key, str)
        assert len(self.prompt.key) == 36

    def test_constructor_returns_with_correct_question(self):
        """Test that when a new Prompt object is instantiated the question
        property matches the question value passed into the constructor
        """
        assert self.prompt.question == QUESTION

    def test_constructor_raises_type_error_for_question_param(self):
        """Test that when the Prompt constructor is called with a non-string
        question argument, a TypeError is raised
        """
        with self.assertRaises(TypeError):
            Prompt(2, RESPONSES_EXPECTED)

    def test_constructor_returns_with_correction_responses_expected(self):
        """Test that when a Prompt object is instantiated the
        responses_expected property matches the value passed into the
        constructor
        """
        assert self.prompt.responses_expected == 2

    def test_constructor_raises_type_error_for_responses_param(self):
        """Test that when the Prompt constructor is called with a non-int
        responses_expected argument, a TypeError is raised
        """
        with self.assertRaises(TypeError):
            Prompt(QUESTION, '2')
