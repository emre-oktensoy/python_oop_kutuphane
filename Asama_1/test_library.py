import pytest
from library import Library, Book, EBook, AudioBook

def test_book_creation():
    book = Book("Test Kitap", "Yazar Adı", "12345")
    assert book.title == "Test Kitap"
    assert book.author == "Yazar Adı"
    assert book.isbn == "12345"

def test_ebook_creation():
    ebook = EBook("E-Kitap", "Dijital Yazar", "99999", 50, "PDF")
    assert ebook.file_size_mb == 50
    assert ebook.file_format == "PDF"
    assert "E-Book" in str(ebook)

def test_audiobook_creation():
    abook = AudioBook("Sesli Kitap", "Anlatıcı", "88888", 120, "Sesli Anlatıcı")
    assert abook.duration_in_minutes == 120
    assert abook.narrator == "Sesli Anlatıcı"
    assert "AudioBook" in str(abook)

def test_library_add_and_find():
    lib = Library()
    book = Book("Python", "Guido", "11111")
    lib.add_book(book)
    found = lib.find_book("11111")
    assert found is not None
    assert found.title == "Python"

def test_library_remove_book():
    lib = Library()
    book = Book("Silinecek", "Yazar", "22222")
    lib.add_book(book)
    lib.remove_book("22222")
    assert lib.find_book("22222") is None

def test_library_list_books(capsys):
    lib = Library()
    lib.list_books()  # boşken
    captured = capsys.readouterr() # çıktıyı yakala
    assert "hiç kitap yok" in captured.out.lower() # boş kütüphane mesajını kontrol et

    lib.add_book(Book("Yeni Kitap", "Yazar", "33333")) # yeni kitap ekle
    lib.list_books()
    captured = capsys.readouterr() # çıktıyı tekrar yakala
    assert "Yeni Kitap" in captured.out # yeni kitabın listede olduğunu kontrol et
