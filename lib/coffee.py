#!/usr/bin/env python3

class Coffee:
    valid_sizes = ["Small", "Medium", "Large"]
    def __init__(self, size, price):
        self._size = None
        self.price = price
        self.size = size
    def get_size(self):
        return self._size
    def set_size(self, value):
        if value in self.valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    size = property(get_size, set_size)
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
