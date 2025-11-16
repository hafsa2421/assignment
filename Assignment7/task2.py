def count_down(n):
    """Count down from n to 0."""
    while n >= 0:
        print(n)
        n -= 1  # Fixed: changed from n += 1 to n -= 1


# Test the function
if __name__ == "__main__":
    print("Countdown from 5:")
    count_down(5)
    
    print("\n" + "=" * 50)
    print("LOGIC ERROR EXPLANATION")
    print("=" * 50)
    print("""
    ERROR IDENTIFIED:
    - Original code: n += 1 (incrementing)
    - Problem: Since condition is n >= 0, incrementing n makes it
      grow forever, causing infinite loop
    
    FIX APPLIED:
    - Changed to: n -= 1 (decrementing)
    - Now n decreases each iteration until it becomes negative
    - Loop terminates when n < 0
    
    EXAMPLE:
    - Input: n = 5
    - Output: 5, 4, 3, 2, 1, 0 (then stops)
    """)
