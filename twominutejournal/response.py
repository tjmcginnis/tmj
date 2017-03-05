"""prompt

A plain Python class representing a journal response
"""
import uuid

class Response:
    """Response

    A container for the properties of a journal response
    """

    def __init__(self, prompt_key: str, response_body: str, key=None):
        """Create a new response

        @param prompt_key:
            The key of the prompt that the response answers
        @param response_body:
            The body of the response
        @param key:
            **Optional**
            If response is instantiated from a persisted response, the key
            value of that response
        """
        if not isinstance(prompt_key, str):
            raise TypeError("prompt_key must be a string")

        if not isinstance(response_body, str):
            raise TypeError("response_text must be a string")

        self.key = key or str(uuid.uuid4())
        self.prompt_key = prompt_key
        self.response_body = response_body
