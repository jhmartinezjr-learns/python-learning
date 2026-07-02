from librarymanager import LibraryBookManager

def main():
    manager = LibraryBookManager()

    while True:
        print("\n=== Library Manager ===")
        print("1. View Books")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Mark Book as Read")
        print("5. Search Books")
        print("6. Update Book")
        print("7. Exit\n")

        choice = input("Select Option: ").strip()

        if choice == "1":
            books = manager.list_books()
            if not books:
                print("Library is Empty.")
            else:
                for b in books:
                    status = "Read" if b.get("read") else "Unread"
                    print(f"{b['id']}. {b['title']} by {b['author']} ({b['year']}) - {status}")

        elif choice == "2":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            try:
                year = int(input("Year: "))
            except ValueError:
                print("Year must be a number.")
                continue
            manager.add_book(title, author, year)

        elif choice == "3":
            try:
                book_id = int(input("Book ID to Delete: "))
                removed = manager.delete_book(book_id)
                if removed:
                    print(f"Deleted: {removed['title']}")
                else:
                    print("Book not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            try:
                book_id = int(input("Book ID to Mark as Read: "))
                updated = manager.mark_as_read(book_id)
                if updated:
                    print(f"Marked as Read: {updated['title']}")
                else:
                    print("Book not Found.")
            except ValueError:
                print("Invalid ID.")
                
        elif choice == "5":
            query = input("What book are you looking for? ")
            results = manager.search_books(query)
            if not results:
                print("No book found")
            else:    
                for book in results:
                    status = "Read" if book.get("read") else "Unread"
                    print(f"{book['id']}. {book['title']} by {book['author']} ({book['year']}) - {status}")

        elif choice =="6":
            query = input("What book would you like to update? ")
            results = manager.search_books(query)
            if not results:
                print("No book found")
            else:
                for book in results:
                    status = "Read" if book.get("read") else "Unread"
                    print(f"{book['id']}. {book['title']} by {book['author']} ({book['year']}) - {status}")
                    
                try:
                    valid_ids = [book["id"] for book in results]
                    book_id = int(input("Select Book ID: "))
                    if book_id not in valid_ids:
                        print("Please choose one of the books shown above")
                        continue
                    
                    title = input("Title: ").strip()
                    author = input("Author: ").strip()
                    year = int(input("Year: "))
                
                    updated = manager.update_book(book_id, title, author, year)
                
                    if updated:
                            print("\nBook Updated Successfully!")
                            print(f"Title : {updated['title']}")
                            print(f"Author: {updated['author']}")
                            print(f"Year  : {updated['year']}")
                            status = "Read" if updated["read"] else "Unread"
                            print(f"Status: {status}\n")
                    else:
                        print("Book ID not Found")
                except ValueError:
                    print("Invalid Input")
                
        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid Selection")


if __name__ == "__main__":
    main()