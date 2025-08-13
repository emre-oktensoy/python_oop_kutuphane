
from dataclasses import dataclass, field
from typing import List
from pydantic import BaseModel, Field, ValidationError
import json
import os


class Book(BaseModel):
    title: str = Field(..., min_length=1)    
    author: List[str] = Field(..., min_length=1)
    isbn: str = Field(..., min_length=10, max_length=13)

    def __str__(self) -> str:
        return f"{self.title} by {', '.join(self.author)} (ISBN: {self.isbn})"


    def to_dict(self):        
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class Library:
    def __init__(self):
        self.name = "City Library"
        self._books = []  

    def add_book(self, book: Book):
        self._books.append(book)
    
    def has_book(self, isbn: str):
        return any(b.isbn == isbn for b in self._books)

    def list_books(self):
       if not self._books:
            print("Kütüphanede hiç kitap yok.")
            return
       for book in self._books:
            print(book)

    def find_book(self, isbn: str) -> Book | None:
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
    
    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if book:
            self._books.remove(book)
            print(f"{book.title} kitabı kütüphaneden kaldırıldı.")
        else:
            print("Kitap bulunamadı.")

    def display_books(self) -> str:
        return "\n".join(str(book) for book in self._books)
    
    def save_to_file(self, filename="library.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self._books], f, indent=4, ensure_ascii=False)

    def load_from_file(self, filename="library.json"):
        if not os.path.exists(filename):
            print(f"{filename} dosyası bulunamadı, kütüphane boş durumda.")
            self._books.clear()
            return
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"{filename} dosyası boş veya geçersiz JSON içeriyor, kütüphane boş durumda.")
            self._books.clear()
            return

        self._books.clear()

        for book_dict in data:                    
            book = Book.from_dict(book_dict)
            self.add_book(book)