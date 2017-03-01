# Two Minute Journal
Two Minute Journal is a library for quick daily gratitude journaling.

## Installation
TODO: Describe the installation process

## Usage
TODO: Describe dependency on a storage adapter for persistence
TODO: Describe portability of application

### Setting it all up
```python
>>> import twominutejournal as journal
>>>
>>> # Basic Storage Adapter implementation
>>> # that adheres to required contract
>>> # but does nothing to persist data
>>> class StorageAdapter:
...     def store_entry(self, entry):
...         pass
...
...     def store_response(self, response):
...         pass
...
...     def get_all_entries(self):
...         return []
...
...     def get_entry_responses(self, response):
...         return []
...
>>> adapter = StorageAdapter()
>>> journal = Journal(adapter)
```

### Get today's prompts
```python
>>> prompts = journal.get_todays_prompts()
>>> prompts
[
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
```

### Write today's entry
```python
>>> entry = journal.create_entry()
>>> responses = []
>>> responses.push(journal.create_response(
...         prompt_id='14e8017e-b9ec-488b-a708-94243a889588',
...         response_text='My hilarious dogs.'))
...
>>> responses.push(journal.create_response(
...         prompt_id='14e8017e-b9ec-488b-a708-94243a889588',
...         response_text='My awesome wife.'))
...
>>> journal.submit_responses(entry, responses)
```

### Retrieve all of a user's entries
```python
>>> entries = journal.view_all_entries()
>>> entries
[
    {
        'id': '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
        'entry_date': '2017-02-01T13:37:27+00:00'
    },
    {
        'id': '0385f421-a980-4b03-9b88-ee67af63c90d',
        'entry_date': '2017-02-01T12:29:13+00:00'
    }
]
```

### Retrieve an entry's responses
```python
>>> entry_id = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'
>>> responses = journal.view_entry_responses(entry_id)
>>> responses
[
    {
        response_id: '6c1de71f-5e99-4dfc-a418-54817b1c73bb',
        entry_id: '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
        prompt_id: '14e8017e-b9ec-488b-a708-94243a889588',
        response_text: 'My hilarious dogs.'
    },
    {
        response_id: 'f7807f94-544c-4795-9f3e-6580b3511a3b',
        entry_id: '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
        prompt_id: '14e8017e-b9ec-488b-a708-94243a889588',
        response_text: 'My awesome wife.'
    },
    ...
]
```

## Contributing
1. Fork it
2. Create your feature branch: `git checkout -b my-new-feature
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
