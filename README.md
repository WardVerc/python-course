# Python: 100 days of code

To keep your dependencies isolated from other projects:

- Create a new virtual environment and install the dependencies:
  - File => Settings => Project => Python Interpreter. Click Add Interpreter => Add Local Interpreter. (PyCharm)
  - Or:
    - First make a virtual environment (venv) for Flask: Run this command in your project folder: `python3 -m venv .venv`
    - Then activate the environment: `. .venv/bin/activate`
    - Finally install Flask in the activated env: pip3 install Flask
