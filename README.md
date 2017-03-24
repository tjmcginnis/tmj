# tmj
`tmj` is a library of functions for daily gratitude (or really any prompt-based) journaling.

## Why tmj?
Because journaling is important to me, but I am short on time and I like having
few possessions. But also...

### It's Simple
`tmj` aims to provide a simple API for prompt-based journaling, allowing you to
create and view prompts, entries, and responses.

### It's Flexibile
Store your data in a database, txt file, Excel file, or whatever else you can
dream up. Persistence is tied to the concept of a storage adapter (implemented
by you), so this library isn't tied to any specific type of persistent storage.

## Installation
`tmj` was written and tested with Python 3.6, and a UNIX shell (bash, zsh, etc.
would all be sufficient). It should work on Linux, OS X, and Windows. Unfortunately,
I have not tested it with earlier versions of Python.

As mentioned, `tmj` is not tied to any specific implementation. As such,
the usage and implementation is up to you. As long as there is a storage adapter
implementation that conforms to the API expected by the functions, anything is
possible!

## Usage

### Setting it all up
```python
>>> import twominutejournal.journal
>>>
>>> class StorageAdapter:
...     '''Basic Storage Adapter implementation
...
...     Does nothing to persist data, but conforms to
...     required contract.
...     '''
...     def store_entry(self, entry):
...         pass
...
...     def store_response(self, response):
...         pass
...
...     def store_prompt(self, prompt):
...         pass
...
...     def get_prompts(self) -> list:
...         return []
...
...     def get_all_entries(self) -> list:
...         return []
...
...     def get_entry_responses(self, entry_id) -> list:
...         return []
...
...     def get_last_entry(self) -> dict:
...         return dict()
...
>>> adapter = StorageAdapter()
```

### Create a prompt
```python
>>> prompt = journal.create_prompt(
        question='I am grateful for...'
        responses_expected=2)
>>> journal.save_prompt(prompt, adapter)
>>> prompt = journal.create_prompt(
        question='Would would make today great?',
        responses_expected=2)
>>> journal.save_prompt(prompt, adapter)
```

### Get today's prompts
```python
>>> prompts = journal.get_todays_prompts(adapter)
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

### Write an entry
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
>>> journal.submit_responses(entry, responses, adapter)
```

### Retrieve all entries
```python
>>> entries = journal.view_all_entries(adapter)
>>> entries
[
    {
        'id': '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
        'timestamp': datetime.datetime(2017, 3, 1, 20, 19, 46, 88453)
    },
    {
        'id': '0385f421-a980-4b03-9b88-ee67af63c90d',
        'timestamp': datetime.datetime(2017, 2, 28, 18, 12, 32, 34442)
    }
]
```

### Retrieve an entry's responses
```python
>>> entry_id = '973d45a3-f2bd-4470-a7c0-b5328c1322bf'
>>> responses = journal.view_entry_responses(entry_id, adapter)
>>> responses
[
    {
        id: '6c1de71f-5e99-4dfc-a418-54817b1c73bb',
        entry_id: '973d45a3-f2bd-4470-a7c0-b5328c1322bf',
        prompt_id: '14e8017e-b9ec-488b-a708-94243a889588',
        response_text: 'My hilarious dogs.'
    },
    {
        id: 'f7807f94-544c-4795-9f3e-6580b3511a3b',
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
