# agro-app
This project were made to shows where and what are good to plant at Sao Paulo State in Brazil. Was made for subject at Information Systems course at UNESP BAURU

## How to run
- Be sure if your Python are successfully working. Open the project's folder. After this, we using Flask to run python at web.

### On Windows (some lib, require install once):
- Create folder named `venv`
- `cd venv`
- `scripts/activate` (if PowerShell does not able to run this command, run `Set-ExecutionPolicy Unrestricted -Scope Process`)
- `cd ..`
- `pip install flask`
- `set FLASK_APP=main.py`
- `$env:FLASK_APP="main.py"`
- `flask run`

Always run inside (venv)

### On Linux (some lib, require install once):
- `sudo apt install python3.8-venv`
- `python3 -m venv venv`
- `cd venv`
- `. bin/activate`
- `cd ..`
- `pip install flask`
- `pip install requests`
- `export FLASK_APP=main.py`
- `flask run`

Always run inside (venv)