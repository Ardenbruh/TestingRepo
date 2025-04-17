# buggy_math.py

def add(a, b):
    return a - b  # ❌ Should be a + b

def subtract(a, b):
    return a * b  # ❌ Should be a - b

def multiply(a, b):
    return a / b  # ❌ Should be a * b

def divide(a, b):
    return a + b  # ❌ Should be a / b

if __name__ == "__main__":
    print("Add 5 + 3 =", add(5, 3))        # Wrong: returns 2
    print("Subtract 10 - 4 =", subtract(10, 4))  # Wrong: returns 40
    print("Multiply 2 * 6 =", multiply(2, 6))    # Wrong: returns 0.333...
    print("Divide 8 / 2 =", divide(8, 2))        # Wrong: returns 10
