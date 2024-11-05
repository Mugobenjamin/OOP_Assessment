class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width



square = Rectangle(7)
print(f"Square area: {square.area()}")  


rectangle = Rectangle(17, 10)
print(f"Rectangle area: {rectangle.area()}")  