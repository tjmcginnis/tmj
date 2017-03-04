"""adapter

Mock storage adapter class for unit tests
"""
class MockStorageAdapter:
    """Mock storage adapter class.

    Will be patched for testing purposes
    """

    def store_entry(self, entry: dict):
        """Mock store_entry"""
        pass

    def store_response(self, response: dict):
        """Mock store_response"""
        pass

    def get_all_entries(self):
        """Mock get_all_entries"""
        pass

    def get_entry_responses(self, entry_id: str):
        """Mock get_entry_responses"""
        pass

    def get_last_entry(self):
        """Mock get_last_entry"""
        pass

    def get_prompts(self):
        """Mock get_prompts"""
        pass
