class Calculator:
    # Static attribute
    count = 0

    @staticmethod
    def add(x, y):
        # count increment
        Calculator.count += 1
        return x + y


# Call the add() method and print results
result1 = Calculator.add(3, 5)
print(f"Result of addition: {result1}")

result2 = Calculator.add(10, 20)
print(f"Result of addition: {result2}")

# Check add() method
print(f"add() method was called {Calculator.count} times.")
