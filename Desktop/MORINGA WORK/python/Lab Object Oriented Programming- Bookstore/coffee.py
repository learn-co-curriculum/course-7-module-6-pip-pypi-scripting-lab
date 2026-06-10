class Coffee:
    def __init__(self, size, price):
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")
            self._size = None
        self.price = price

    @property
    def size(self):
        return self._size

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
