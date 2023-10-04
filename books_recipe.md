# {{books}} Model and Repository Classes Design Recipe

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.


## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, author_name FROM books;

        # Returns an array of Book objects.
   
```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# _________________ Unit test Book class ___________________

"""
When we construct a Book object
We can get back the id, title and author_name attributes
"""
def test_constructs():
    book = Book(1, "Test Title", "Test Author")
    book.id == 1
    book.title == "Test Title"
    book.author_name == "Test Author"

"""
When we compare two identical Book objects
They are considered equal
"""
def test_identical_book_objects_considered_equal():
    book_1 = Book(1, "Test Title", "Test Author")
    book_2 = Book(1, "Test Title", "Test Author")
    book_1 == book_2

"""
When we contsruct a Book object and conveert it to a string
It prints in a user friendly format
"""
def test_string_book_object_formats_nicely():
    book = Book(1, "Test Title", "Test Author")
    str(book) == "Book(1, Test Title, Test Author)"

# _________________ Integration test BookRepository _________________

"""
When we call BookRepository#all
We get a list of Book objects which reflect the seed data
"""
def test_all_returns_list_of_book_objects(db_connection):
    db_connection.seed("seeds/book_store.sql")
    book_repository = BookRepository(db_connection)
    books = book_repository.all()
    books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
