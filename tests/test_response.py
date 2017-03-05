"""test_response

Tests for the Response class of twominutejournal
"""
import unittest

from twominutejournal.response import Response


PROMPT = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'
BODY = "My hilarious dogs."

class TestResponse(unittest.TestCase):
    """Tests for Response"""

    def setUp(self):
        """Create a Response instance for test suite"""
        self.response = Response(PROMPT, BODY)

    def test_constructor_returns_with_valid_key(self):
        """Test that when a new Response object is instantiated the key
        property contains a 36 character string
        """
        assert isinstance(self.response.key, str)
        assert len(self.response.key) == 36

    def test_constructor_sets_key_if_present(self):
        """Test that if a key parameter is passed in, it it set as the
        Response object's key
        """
        key = '14e8017e-b9ec-488b-a708-94243a889588'
        response = Response(PROMPT, BODY, key)

        assert response.key == key

    def test_constructor_returns_with_correct_prompt_key(self):
        """Test that when a Response object is instantiated the
        prompt_key property matches the value passed in to the
        constructor
        """
        assert self.response.prompt_key == PROMPT

    def test_constructor_raises_type_error_prompt_key(self):
        """Test that Response constructor raises a TypeError if the
        prompt_key argument is not of type str
        """
        with self.assertRaises(TypeError):
            Response(5, BODY)

    def test_constructor_returns_with_correct_response_body(self):
        """Test that when a Response object is instantiated the
        response_body property matches the value passed in the
        constructor
        """
        assert self.response.response_body == BODY

    def test_constructor_raises_type_error_response_body(self):
        """Test that Response constructor raises a TypeError if the
        response_body argument is not of type str
        """
        with self.assertRaises(TypeError):
            Response(PROMPT, 5)
