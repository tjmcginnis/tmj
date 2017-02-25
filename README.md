# Two Minute Journal
TODO: Write project description

## Installation
TODO: Describe the installation process

## Usage
TODO: Write usage instructions

### Setting it all up
```python
>>> class StorageAdapter:
...
...     def store_entry(self, entry):
...         pass
...         
...     def store_response(self, response):
...         pass
...
...     def get_all_entries(self, response):
...         pass
...
...     def get_entry_responses(self, response):
...         pass
...
...     def store_user(self, user):
...         pass
...
...     def get_user(self, user):
...         pass
...
...     def update_user(self, user):
...         pass
...
...     def delete_user(self, user):
...         pass
...
...     def get_user_from_token(self, token):
...         pass
...
>>> storage_adapter = StorageAdapter()
```

### Create a new user
```python
>>> user = {
        'email': 'journalUser@gmail.com', 
        'password_digest': b'$2b$12$DYN7AGkZ4bXhGlaLKZ04OuNCm0VRS.UxIftOd5yrkoReH12mlr/gS'
    }
>>> journal.create_user(user, storage_adapter)
```

### Log a user in
```python
>>> email = 'journalUser@gmail.com'
>>> password = b'secret password'
>>> token = journal.log_in(email, password, storage_adapter)
>>> token
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
```

### Get today's prompts
```python
>>> prompts = journal.get_todays_prompts(token, storage_adapter)
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
>>> entry = journal.create_entry(token)
>>> responses = []
>>> responses.push(journal.create_response(
...         prompt_id='14e8017e-b9ec-488b-a708-94243a889588', 
...         response_text='My hilarious dogs.'))
...
>>> responses.push(journal.create_response(
...         prompt_id='14e8017e-b9ec-488b-a708-94243a889588', 
...         response_text='My awesome wife.'))
...
>>> journal.submit_responses(entry, responses, storage_adapter)
```

### Retrieve all of a user's entries
```python
>>> entries = journal.view_all_entries(token, storage_adapter)
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
>>> responses = journal.view_entry_responses(entry_id, storage_adapter)
>>> responses
[
    {
        response_id='6c1de71f-5e99-4dfc-a418-54817b1c73bb',
        prompt_id='14e8017e-b9ec-488b-a708-94243a889588', 
        response_text='My hilarious dogs.'
    },
    {
        response_id='f7807f94-544c-4795-9f3e-6580b3511a3b',
        prompt_id='14e8017e-b9ec-488b-a708-94243a889588', 
        response_text='My awesome wife.'
    },
    ...
]
```

### Log a user out
```python
>>>> journal.log_out(token, storage_adapter)
```

## Contributing
1. Fork it
2. Create your feature branch: `git checkout -b my-new-feature
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## History
TODO: Write history

## License
TODO: Write license
