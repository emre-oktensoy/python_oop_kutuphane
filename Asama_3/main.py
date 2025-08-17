from library import Library, Book
import httpx
import json

def main():
    library = Library()
    library.load_from_file()  # Kitapları dosyadan yükle

    while True:
        print("\n--- Kütüphane Menüsü ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminizi yapınız (1-5): ").strip()

        if choice == "1":
            # Kitap Ekleme - Bu bölümde Open Library API'si kullanılacak
            
            isbn = input("Kitap ISBN: ").strip()
            OPEN_LIBRARY_URL = "https://openlibrary.org/search.json"  
                      
            params = {"isbn": isbn}
            
            if library.has_book(isbn):
                print("Bu kitap zaten kütüphanede mevcut.")
                continue
            try:
                response = httpx.get(OPEN_LIBRARY_URL, params=params)
                #response = httpx.get("https://openlibrary.invalid-domain") test amaçlı hata     
                response.raise_for_status()

                data = response.json()                
                if data.get('docs'):
                    
                    first_book = data['docs'][0]                   
                    title=first_book.get('title')
                    author=first_book.get('author_name')
                    
                    book = Book(title=title, author=author, isbn=isbn)
                    library.add_book(book)
                    print(f"'{title}' kitabı eklendi.")
                else:
                    print("Kitap bulunmadığından eklenemedi.")
            except httpx.HTTPStatusError as e:
                print(f"Hata! API yanıtı: {e.response.status_code} - {e.response.text}")
            except httpx.RequestError as e:
                print(f"İstek hatası: {e}") 
            

        elif choice == "2":
            # Kitap Silme
            isbn = input("Silinecek kitabın ISBN numarası: ").strip()
            library.remove_book(isbn)

        elif choice == "3":
            # Kitapları Listele
            library.list_books()

        elif choice == "4":
            # Kitap Ara
            isbn = input("Aranacak kitabın ISBN numarası: ").strip()
            book = library.find_book(isbn)
            if book:
                print("Kitap bulundu:")
                print(book)
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            # Çıkış
            library.save_to_file()
            print("Değişiklikler kaydedildi. Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
