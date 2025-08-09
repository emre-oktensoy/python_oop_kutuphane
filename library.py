
from dataclasses import dataclass, field
from typing import List
from pydantic import BaseModel, Field, ValidationError
import json
import os

class Book:    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn       
    
    def __str__(self)-> str:
         return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"])
    
class EBook(Book):
    def __init__(self, title: str, author: str, isbn: str, file_size_mb: int, file_format: str):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb
        self.file_format = file_format     

    def __str__(self)-> str:
        return (f"{super().__str__()} [E-Book: {self.file_size_mb}MB, Format: {self.file_format}]")

    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "EBook",
            "file_size_mb": self.file_size_mb,
            "file_format": self.file_format
        })
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["file_size_mb"],
            data["file_format"]
        )

class AudioBook(Book):
    def __init__(self, title: str, author: str, isbn: str, duration_in_minutes: int, narrator: str):
        super().__init__(title, author, isbn)
        self.duration_in_minutes = duration_in_minutes
        self.narrator = narrator

    def __str__(self) -> str:
        return (f"{super().__str__()} [AudioBook: {self.duration_in_minutes} mins, Narrated by {self.narrator}]")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "AudioBook",
            "duration_in_minutes": self.duration_in_minutes,
            "narrator": self.narrator
        })
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["duration_in_minutes"],
            data["narrator"]
        )

class Library:
    def __init__(self):
        self.name = "City Library"
        self._books = []  

    def add_book(self, book: Book):
        self._books.append(book)
    
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
            book_type = book_dict.get("type")  # 'Book', 'EBook' veya 'AudioBook'

            if book_type == "EBook":
                book = EBook.from_dict(book_dict)
            elif book_type == "AudioBook":
                book = AudioBook.from_dict(book_dict)
            else:
                book = Book.from_dict(book_dict)

            self.add_book(book)