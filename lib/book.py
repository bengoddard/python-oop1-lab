#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count
    def get_page(self):
        return self._page_count
    def set_page(self, value):
        if type(value) is int:
            self._page_count = value
        else:
            print("page_count must be an integer")
    page_count = property(get_page, set_page)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book1 = Book("Test Title", "not an integer")
print(book1.page_count)