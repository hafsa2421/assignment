def divide(a, b):
    """Divide a by b with error handling for division by zero."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None


# Test the function
if __name__ == "__main__":
    print("=" * 50)
    print("DIVISION FUNCTION WITH ERROR HANDLING")
    print("=" * 50)
    
    # Test cases
    print("\n1. Normal division:")
    print(f"divide(10, 2) = {divide(10, 2)}")
    
    print("\n2. Division by zero (with error handling):")
    result = divide(10, 0)
    if result is None:
        print("Function returned None due to error")
    
    print("\n3. Another normal division:")
    print(f"divide(15, 3) = {divide(15, 3)}")
    
    print("\n" + "=" * 50)
    print("DEBUG EXPLANATION")
    print("=" * 50)
    print("""
    RUNTIME ERROR IDENTIFIED:
    - Original code: return a / b (no error handling)
    - Problem: Dividing by zero raises ZeroDivisionError
    - This causes program to crash
    
    FIX APPLIED:
    - Added try-except block to catch ZeroDivisionError
    - Returns None and prints error message when division by zero occurs
    - Program continues running instead of crashing
    
    ALTERNATIVE FIXES:
    - Could also check if b == 0 before dividing
    - Could raise a custom exception
    - Could return a default value or float('inf')
    """)
