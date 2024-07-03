# M1 Motors Chatbot Project 

## Requirements
* Python 3.7.9

## Installation
- Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Option 1 - WebServer
- Set the Flask envirenment
```sh
set FLASK_APP=chatbot.py
```

- Run the web version
```sh
flask run
```
### Option 2 - Terminal
- Run the terminal version
```sh
python chatbot.py
```

## FAQ
1 - Error when trying to run the app
Execute
```sh
python -m spacy download en_core_web_md

python -m spacy link en_core_web_md en
```

## Testing
To run the testing file execute:
```sh
python -m unittest test_chatbot.py
```