# Original code that causes IndexError
numbers = [1, 2, 3]
# print(numbers[5])  # IndexError: list index out of range


# Solution 1: Try-except block
def safe_access_try_except(numbers, index):
    try:
        return numbers[index]
    except IndexError:
        print(f"Error: Index {index} out of range. List has {len(numbers)} elements.")
        return None


# Solution 2: Check length before access
def safe_access_check_length(numbers, index):
    if 0 <= index < len(numbers):
        return numbers[index]
    else:
        print(f"Error: Index {index} out of range. Valid: 0 to {len(numbers) - 1}")
        return None


# Solution 3: Safe access with default value
def safe_access_default(numbers, index, default=None):
    return numbers[index] if 0 <= index < len(numbers) else default


# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("TASK #5: INDEXERROR RESOLUTION")
    print("=" * 50)
    
    numbers = [1, 2, 3]
    print(f"List: {numbers}, Length: {len(numbers)}")
    print("Problem: print(numbers[5]) causes IndexError\n")
    
    index = 5
    print(f"Accessing index {index}:")
    print(f"1. Try-Except: {safe_access_try_except(numbers, index)}")
    print(f"2. Check Length: {safe_access_check_length(numbers, index)}")
    print(f"3. Default Value: {safe_access_default(numbers, index, 'Not Found')}")
    
    print(f"\nValid index (1): {safe_access_check_length(numbers, 1)}")
    
    print("\n" + "=" * 50)
    print("AI RECOMMENDATIONS")
    print("=" * 50)
    print("""
    1. CHECK LENGTH: if 0 <= index < len(list)
       - Prevents IndexError, most efficient
    
    2. USE TRY-EXCEPT: Catch IndexError gracefully
       - Good for error handling
    
    3. SAFE ACCESS: Return default for invalid indices
       - Clean and simple approach
    
    RECOMMENDED: Check length before access is best.
    """)
