import json

class LibraryBookManager:
    def __init__(self, filename="booklibrary.json"):
        self.filename = filename
        self.books = self.load_books()
        
    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)
            
    def add_book(self, title, author, year):
        book = {
            "id": self._next_id(),
            "title": title,
            "author": author,
            "year": int(year),
            "read": False
        }
        self.books.append(book)
        self.save_books()
        return book
        
    def list_books(self):
        return self.books
            
    def delete_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.get("id") == book_id:
                removed = self.books.pop(i)
                self.save_books()
                return removed
        return None
    
    def mark_as_read(self, book_id):
        for book in self.books:
            if book.get("id") == book_id:
                book["read"] = True
                self.save_books()
                return book
        return None
    
    def _next_id(self):
        if not self.books:
            return 1
        return max(b.get("id", 0) for b in self.books) + 1
    
    def search_books(self, query):
        results = []
        for book in self.books:
            if (
                query.lower() in book["title"].lower()
                or query.lower() in book["author"].lower()
                or query in str(book["year"])
            ):
                results.append(book)
        return results
    
    def update_book(self, book_id, title, author, year):
        for book in self.books:
            if book.get("id") == book_id:
                book["title"] = title
                book["author"] = author
                book["year"] = int(year)
                self.save_books()
                return book
        return None
    
    def toggle_read(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                book["read"] = not book["read"]
                self.save_books()
                return book
        return None