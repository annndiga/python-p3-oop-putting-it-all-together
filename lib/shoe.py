#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def cobble(self):
       if not isinstance(self.size, int):
            error_message = f"size must be an integer for shoe '{self.brand}', got type {type(self.size).__name__}"
            raise TypeError(error_message)
       print("Your shoe is as good as new!")
       self.condition = "New"

       
        
       

        