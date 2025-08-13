import pytest
import httpx
from library import Library, Book


@pytest.fixture
def sample_library():
    lib = Library()
    book1 = Book(title="Dune", author=["Frank Herbert"], isbn="9780441013593")
    book2 = Book(title="Matilda", author=["Roald Dahl"], isbn="9780140328721")


    lib.add_book(book1)
    lib.add_book(book2)
    return lib

def test_add_book(sample_library):
    new_book = Book(title="1984", author=["George Orwell"], isbn="9780451524935")
    sample_library.add_book(new_book)
    assert sample_library.has_book("9780451524935")

def test_has_book(sample_library):
    assert sample_library.has_book("9780441013593") is True
    assert sample_library.has_book("0000000000000") is False

def test_find_book(sample_library):
    book = sample_library.find_book("9780140328721")
    assert book is not None
    assert book.title == "Matilda"

def test_remove_book(sample_library):
    sample_library.remove_book("9780441013593")
    assert sample_library.has_book("9780441013593") is False

def test_display_books(sample_library):
    output = sample_library.display_books()
    assert "Dune by Frank Herbert" in output
    assert "Matilda by Roald Dahl" in output

def test_save_and_load(tmp_path):
    lib = Library()
    book = Book(title="Test Book", author=["Test Author"], isbn="1234567890123")
    lib.add_book(book)

    file_path = tmp_path / "test_library.json"
    lib.save_to_file(file_path)

    new_lib = Library()
    new_lib.load_from_file(file_path)

    assert new_lib.has_book("1234567890123")
    loaded_book = new_lib.find_book("1234567890123")
    assert loaded_book.title == "Test Book"

def test_openlibrary_connection():
    url = "https://openlibrary.org/search.json"
    params = {"title": "Dune"}

    try:
        response = httpx.get(url, params=params, timeout=5)
        response.raise_for_status()
    except httpx.RequestError as e:
        pytest.fail(f"Bağlantı hatası: {e}")
    except httpx.HTTPStatusError as e:
        pytest.fail(f"Sunucu hatası: {e.response.status_code} - {e.response.text}")