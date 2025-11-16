class Rectangle:
    """Rectangle class with length and width attributes."""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)


# Test the class
if __name__ == "__main__":
    print("=" * 50)
    print("RECTANGLE CLASS - ERROR FIXED")
    print("=" * 50)
    
    # Create rectangle object
    rect = Rectangle(5, 3)
    print(f"\nRectangle created: length={rect.length}, width={rect.width}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    print("\n" + "=" * 50)
    print("ERROR IDENTIFICATION AND FIX")
    print("=" * 50)
    print("""
    ERROR IDENTIFIED:
    - Original code: def __init__(length, width):
    - Problem: Missing 'self' parameter as first argument
    - This causes TypeError when creating an object
    
    FIX APPLIED:
    - Changed to: def __init__(self, length, width):
    - 'self' is now the first parameter
    - This is required for all instance methods in Python
    
    EXPLANATION:
    - In Python, 'self' refers to the instance of the class
    - All instance methods must have 'self' as first parameter
    - Without 'self', Python doesn't know which object to work with
    - The constructor now correctly initializes instance attributes
    
    BEFORE (incorrect):
        def __init__(length, width):
            self.length = length  # ❌ Error: self not defined
    
    AFTER (correct):
        def __init__(self, length, width):
            self.length = length  # ✅ Correct: self is parameter
    """)

