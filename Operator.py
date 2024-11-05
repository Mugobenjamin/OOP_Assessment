class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            # Add vectors
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"



# Create  vector objects
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

# Add the vectors
result_vector = vector1 + vector2

print(f"Result of adding {vector1} and {vector2} is {result_vector}.")
