from fastapi import Body, Query, Path
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from library import Library, Book 
from typing import List
import httpx


app = FastAPI(title="Library API")

class ISBNRequest(BaseModel):
    isbn: str = Field(..., min_length=10, max_length=13, description="Kitabın ISBN numarası") #FastAPI’de JSON body için bir Pydantic model tanımladık

OPEN_LIBRARY_URL = "https://openlibrary.org/search.json"

library = Library()       # Kütüphane nesnesi oluşturduk
library.load_from_file()  # Dosyadaki kitapları yüklüyoruz



# GET /books endpoint ########################
@app.get("/books", response_model=List[Book])   # response_model=List[Book] -> Dönen veriyi Book modeline uygun JSON olarak otomatik seri hale getirir.
def get_books():
    """
    Kütüphanedeki tüm kitapları JSON olarak döndürür.
    """
    return library.get_books_as_list()  # Pydantic modeli olduğu için otomatik JSON'a dönüştürebiliyoruz

    
# GET /books/{isbn} endpoint ##################   
@app.delete("/books/{isbn}", status_code=204)
def delete_book(isbn: str):
    """
    ISBN'e göre kitabı kütüphaneden siler.
    """
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

    library.remove_book(isbn)
    library.save_to_file()  # Kalıcı silme
    return  # 204 No Content döndürür



# POST /books endpoint ########################
@app.post("/books")
def add_book(isbn_request: ISBNRequest):
    """
    JSON body'den ISBN alır, Open Library API'den veri çeker,
    kitabı kütüphaneye ekler ve eklenen kitabı döndürür.
    """
    isbn = isbn_request.isbn

    # 1 Kitap zaten var mı kontrol et
    if library.has_book(isbn):
        raise HTTPException(status_code=400, detail="Bu kitap zaten kütüphanede mevcut.")

    # 2 Open Library API çağrısı
    try:
        response = httpx.get(OPEN_LIBRARY_URL, params={"isbn": isbn})
        response.raise_for_status()  
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"API isteği başarısız: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"API yanıt hatası: {e.response.status_code}")

    data = response.json()

    # 3️ API verisi boş mu kontrol et
    if not data.get("docs"):
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

    first_book = data["docs"][0]
    title = first_book.get("title")
    author = first_book.get("author_name")

    # 4️ Book nesnesi oluştur ve ekle
    book = Book(title=title, author=author, isbn=isbn)
    library.add_book(book)
    library.save_to_file()  # Kütüphaneyi dosyaya kaydet

    # 5️ Başarılı ekleme → JSON olarak döndür
    return book.to_dict()
