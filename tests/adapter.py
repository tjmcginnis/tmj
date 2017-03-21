"""
    tests.adapter
    ~~~~~~~~~~~~~

    A skeleton storage interface adapter class
    for mocking during unit tests.
"""


class MockStorageAdapter:
    '''MockStorageAdapter'''

    def store_entry(self, entry: dict):
        '''store_entry'''
        pass

    def store_response(self, response: dict, entry_key: int):
        '''store_response'''
        pass

    def get_all_entries(self):
        '''get_all_entries'''
        pass

    def get_entry_responses(self, entry_id: str):
        '''get_entry_responses'''
        pass

    def get_last_entry(self):
        '''get_last_entry'''
        pass

    def get_prompts(self):
        '''get_prompts'''
        pass
