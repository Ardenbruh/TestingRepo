# buggy_math.py

def add(a, b):
    return a - b  # ❌ Incorrect: should be a + b

def subtract(a, b):
    return a * b  # ❌ Incorrect: should be a - b

def multiply(a, b):
    return a / b  # ❌ Incorrect: should be a * b

def divide(a, b):
    return a + b  # ❌ Incorrect: should be a / b

if __name__ == "__main__":
    print("Add 10 + 5 =", add(10, 5))         # Incorrect: 5
    print("Subtract 10 - 5 =", subtract(10, 5)) # Incorrect: 50
    print("Multiply 10 * 5 =", multiply(10, 5)) # Incorrect: 2.0
    print("Divide 10 / 5 =", divide(10, 5))     # Incorrect: 15
