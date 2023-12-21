# Book Store Database

## Introduction
- This is my first coach assessed challenge in Makers Module 3 - Databases
- I set up this project using a starter project from Makers, as per the challenge instructions below.
- This project includes a `book_store` database, containing a `books` table.
- The main program `app.py` prints a list of all the books in the database to the terminal.
- `books_recipe.md` documents my design of the `Book` and `BookRepository` classes, as well as the relevant tests to test-drive development


## Objectives
Test-drive a `Book` class and a `BookRepository` class with an all method:
- [x] Set up a new project called book_store from the starter.
- [x] Use the book_store SQL seed instead of the music_library seed. You can find this in the seeds directory in the starter.
- [x] Create the design recipe as usual, before starting to test-drive the classes.
- [x] Test-drive a `Book` class that has attributes for each column in the books table, using the example(s) from your design.
- [x] Test-drive a `BookRepository` class that has a method all that returns a list of `Book` objects.
- [x] Write a small program in `app.py` using the class `BookRepository` to print out the list of books to the terminal.
You should get an output that looks roughly like this:
```shell
# In the project directory book_store

; pipenv shell
; python app.py

1 - Nineteen Eighty-Four - George Orwell
2 - Mrs Dalloway - Virginia Woolf
3 - Emma - Jane Austen
4 - Dracula - Bram Stoker
5 - The Age of Innocence - Edith Wharton
```

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...

# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/book-store-database.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell
# NB: you may need to change interpreter path, to import pytest and psycopg
# This will give you the path to use
; pipenv --venv

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py

# To exit the pipenv shell
; exit # or Ctrl-D
