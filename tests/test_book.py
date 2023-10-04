from lib.book import Book

"""
When we construct a Book object
We can get back the id, title and author_name attributes
"""
def test_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"

"""
When we compare two identical Book objects
They are considered equal
"""
def test_identical_book_objects_considered_equal():
    book_1 = Book(1, "Test Title", "Test Author")
    book_2 = Book(1, "Test Title", "Test Author")
    assert book_1 == book_2

"""
When we contsruct a Book object and convert it to a string
It prints in a user friendly format
"""
def test_string_book_object_formats_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "1 - Test Title - Test Author"