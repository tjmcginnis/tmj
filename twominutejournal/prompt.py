"""prompt

A plain Python class representing a gratitude journal's prompts
"""
import uuid

class Prompt:
    """Prompt

    A container for the identifying properties of a journal prompt
    """

    def __init__(self, question: str, responses_expected: int):
        """Create a new prompt

        @param question:
            String representing the question to respond to
        @param responses_expected:
            The number of unique responses expected for the prompt
        """
        if not isinstance(question, str):
            raise TypeError("question must be a string")

        if not isinstance(responses_expected, int):
            raise TypeError("responses_expected must be an integer")

        self.key = str(uuid.uuid4())
        self.question = question
        self.responses_expected = responses_expected
