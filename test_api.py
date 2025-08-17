from fastapi.testclient import TestClient
from api import app, library

client = TestClient(app)

TEST_ISBN = "9780140328721"
TEST_BOOK = {"isbn": TEST_ISBN}

def test_get_books_initially_empty():
    library._books.clear()
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book_success():
    library._books.clear()
    response = client.post("/books", json=TEST_BOOK)
    assert response.status_code == 200
    data = response.json()
    assert data["isbn"] == TEST_ISBN
    assert "title" in data
    assert "author" in data

def test_add_book_duplicate():
    library._books.clear()
    client.post("/books", json=TEST_BOOK)  # İlk ekleme
    response = client.post("/books", json=TEST_BOOK)  # Tekrar ekleme
    assert response.status_code == 400
    assert response.json()["detail"] == "Bu kitap zaten kütüphanede mevcut."

def test_delete_book_success():
    library._books.clear()
    client.post("/books", json=TEST_BOOK)  # Kitabı ekle
    response = client.delete(f"/books/{TEST_ISBN}")
    assert response.status_code == 204

def test_delete_book_not_found():
    library._books.clear()
    response = client.delete("/books/0000000000000")
    assert response.status_code == 404
    assert response.json()["detail"] == "Kitap bulunamadı."