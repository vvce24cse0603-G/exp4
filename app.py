import unittest

# Application code
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


# Automated test cases
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(50, 20), 70)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)


# Main application
if __name__ == "__main__":

    print("Student Calculator Application")
    print("Addition:", add(50, 20))
    print("Subtraction:", subtract(20, 10))
    print("Multiplication:", multiply(5, 4))

    print("\nExecuting Automated Tests...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
