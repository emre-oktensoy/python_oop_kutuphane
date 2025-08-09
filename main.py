from library import Library, Book, EBook, AudioBook

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
            # Kitap Ekleme
            title = input("Kitap başlığı: ").strip()
            author = input("Yazar: ").strip()
            isbn = input("ISBN: ").strip()
            book_type = input("Kitap türü (Book / EBook / AudioBook) [Book]: ").strip().lower()

            if book_type == "ebook":
                try:
                    file_size_mb = int(input("Dosya boyutu (MB): ").strip())
                except ValueError:
                    print("Geçersiz dosya boyutu. Kitap eklenemedi.")
                    continue
                file_format = input("Dosya formatı: ").strip()
                book = EBook(title, author, isbn, file_size_mb, file_format)

            elif book_type == "audiobook":
                try:
                    duration_in_minutes = int(input("Süre (dakika): ").strip())
                except ValueError:
                    print("Geçersiz süre. Kitap eklenemedi.")
                    continue
                narrator = input("Seslendiren: ").strip()
                book = AudioBook(title, author, isbn, duration_in_minutes, narrator)

            else:
                book = Book(title, author, isbn)

            library.add_book(book)
            print(f"'{title}' kitabı eklendi.")

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
