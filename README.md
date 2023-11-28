# agro-app
This project were made to shows where and what are good to plant at Sao Paulo State in Brazil. Was made for subject at Information Systems course at UNESP BAURU

## How to run
- Be sure if your Python are successfully working. Open the project's folder. After this, we using Flask to run python at web.

### On Windows Powershell:
- `python -m venv venv`
- `cd venv`
- `scripts/activate` (if PowerShell does not able to run this command, run `Set-ExecutionPolicy Unrestricted -Scope Process`)
- `cd ..`
- `pip install -r requirements.txt`
- `set FLASK_APP=main.py`
- `$env:FLASK_APP="main.py"`
- `flask run`

Always run `flask run` inside (venv)

## In case of CSS are not correct, go to root and run these commands (NodeJS and NPM needed):
- `npm install`
- `npm run buildcss`

### On Linux or MacOS (some lib, require install once and NodeJS are require to run NPM commands):
- `python3 -m venv venv` or `python -m venv venv`
- `cd venv`
- `. bin/activate`
- `cd ..`
- `pip install -r requirements.txt`
- `export FLASK_APP=main.py` 
- `flask run`

Always run `flask run` inside (venv)

## In case of CSS are not correct, go to root and run these commands (NodeJS and NPM needed):
- `npm install`
- `npm run buildcss`