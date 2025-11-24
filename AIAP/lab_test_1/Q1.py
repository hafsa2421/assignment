
def factorial_recursive(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Args:
        n (int): A non-negative integer for which to calculate the factorial.
    
    Returns:
        int: The factorial of n (n!).
    
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    
    Note:
        This recursive implementation may raise RecursionError for very large
        values of n due to Python's recursion limit.
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError(f"factorial_recursive() expects an integer, got {type(n).__name__}")
    
    # Handle negative numbers
    if n < 0:
        raise ValueError(f"factorial_recursive() not defined for negative numbers, got {n}")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)


# ============================================================================
# TESTING THE FUNCTION
# ============================================================================

if __name__ == "__main__":
    # Test cases for normal inputs
    print("Testing normal inputs:")
    print(f"factorial(0) = {factorial(0)}")      # Expected: 1
    print(f"factorial(1) = {factorial(1)}")      # Expected: 1
    print(f"factorial(5) = {factorial(5)}")      # Expected: 120
    print(f"factorial(10) = {factorial(10)}")    # Expected: 3628800
    
    print("\nTesting edge cases:")
    
    # Test negative input (should raise ValueError)
    try:
        result = factorial(-1)
        print(f"factorial(-1) = {result}")
    except ValueError as e:
        print(f"factorial(-1) raised ValueError: {e}")
    
    # Test non-integer input (should raise TypeError)
    try:
        result = factorial(5.5)
        print(f"factorial(5.5) = {result}")
    except TypeError as e:
        print(f"factorial(5.5) raised TypeError: {e}")
    
    # Test zero (should return 1)
    print(f"factorial(0) = {factorial(0)}")
    
    print("\nComparing iterative vs recursive:")
    print(f"factorial(7) = {factorial(7)}")
    print(f"factorial_recursive(7) = {factorial_recursive(7)}")

