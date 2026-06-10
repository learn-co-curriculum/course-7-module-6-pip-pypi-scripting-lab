class Book:
    def __init__(self, title, page_count):
        self.title = title
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = 0

    @property
    def page_count(self):
        return self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
