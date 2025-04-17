# correct_math.py

def add(a, b):
    return a + b  # ✅ Correct

def subtract(a, b):
    return a - b  # ✅ Correct

def multiply(a, b):
    return a * b  # ✅ Correct

def divide(a, b):
    if b != 0:
        return a / b  # ✅ Correct
    else:
        return "Error: Division by zero"

if __name__ == "__main__":
    print("Add 10 + 5 =", add(10, 5))         # Output: 15
    print("Subtract 10 - 5 =", subtract(10, 5)) # Output: 5
    print("Multiply 10 * 5 =", multiply(10, 5)) # Output: 50
    print("Divide 10 / 5 =", divide(10, 5))     # Output: 2.0
