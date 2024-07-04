# M1 Motors Chatbot Project 

## Requirements
* Python 3.7.9
* Administrator permissions to run the terminal

## Installation
1 - Clone the repository:
```sh
git clone https://github.com/mmolinarijr/m1-project.git
cd m1-project
```

2 - Set up a virtual environment (optional but recommended):
```sh
python -m venv venv
source env/bin/activate  # On Windows run `\venv\Scripts\activate.bat`
```
If you have multiple Python versions installed, ensure to use the required version to create the environment. You can also use pyenv to manage multiple Python versions.

3 - Install dependencies:
```sh
pip install -r requirements.txt
```

4 - Set up spaCy model reference:
* Run the following commands:
```sh
python -m spacy download en_core_web_md

python -m spacy link en_core_web_md en --force
```

## Usage
### Option 1 - WebServer
- Set Flask environment:

Windows
```sh
set FLASK_APP=chatbot.py
```
Linux/Mac/Unix
```sh
export FLASK_APP=chatbot.py
```

- Run the web version:
```sh
flask run
```
### Option 2 - Terminal
- Run the terminal version:
```sh
python chatbot.py
```

## FAQ
1 - App not running or problems installing the dependencies:
* Make sure you have Python 3.7.9 installed and activated in your environment.

## Testing
To run tests, execute the following command:
```sh
python -m unittest test_chatbot.py
```