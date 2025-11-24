Student Marks Analysis with Prompting Techniques Demonstration

This file demonstrates three different prompting approaches:
1. Zero-shot prompting
2. One-shot prompting
3. Few-shot prompting
"""


# ============================================================================
# PROBLEM STATEMENT
# ============================================================================
# Given a list of student marks, compute the mean and list all students
# above the mean.
# ============================================================================


# ============================================================================
# ZERO-SHOT PROMPT APPROACH
# ============================================================================
# Prompt: "Given a list of student marks, compute the mean and list all
#          students above the mean."
#
# Characteristics:
# - No examples provided
# - AI must figure out the approach from scratch
# - Relies on general knowledge and reasoning
# ============================================================================

def analyze_marks_zero_shot(students_marks):
    """
    Analyze student marks using zero-shot approach.
    
    Args:
        students_marks (list): List of tuples (student_name, mark)
    
    Returns:
        dict: Dictionary containing mean and students above mean
    """
    if not students_marks:
        return {"mean": 0, "above_mean": []}
    
    # Calculate mean
    total = sum(mark for _, mark in students_marks)
    mean = total / len(students_marks)
    
    # Find students above mean
    above_mean = [(name, mark) for name, mark in students_marks if mark > mean]
    
    return {
        "mean": mean,
        "above_mean": above_mean
    }


# ============================================================================
# ONE-SHOT PROMPT APPROACH
# ============================================================================
# Prompt: "Given a list of student marks, compute the mean and list all
#          students above the mean.
#
#          Example:
#          Input: [('Alice', 85), ('Bob', 90), ('Charlie', 75), ('Diana', 95)]
#          Output:
#          Mean: 86.25
#          Students above mean: [('Bob', 90), ('Diana', 95)]"
#
# Characteristics:
# - One example provided
# - Shows expected format and approach
# - Helps AI understand the structure better
# ============================================================================

def analyze_marks_one_shot(students_marks):
    """
    Analyze student marks using one-shot approach.
    
    Following the pattern shown in the example:
    - Calculate mean of all marks
    - Return students with marks strictly greater than mean
    
    Args:
        students_marks (list): List of tuples (student_name, mark)
    
    Returns:
        dict: Dictionary containing mean and students above mean
    """
    if not students_marks:
        return {"mean": 0.0, "above_mean": []}
    
    # Extract marks and calculate mean
    marks = [mark for _, mark in students_marks]
    mean = sum(marks) / len(marks)
    
    # Filter students above mean (strictly greater than)
    above_mean = [(name, mark) for name, mark in students_marks if mark > mean]
    
    return {
        "mean": mean,
        "above_mean": above_mean
    }


# ============================================================================
# FEW-SHOT PROMPT APPROACH
# ============================================================================
# Prompt: "Given a list of student marks, compute the mean and list all
#          students above the mean.
#
#          Examples:
#          1. Input: [('Alice', 85), ('Bob', 90), ('Charlie', 75), ('Diana', 95)]
#             Output:
#             Mean: 86.25
#             Students above mean: [('Bob', 90), ('Diana', 95)]
#
#          2. Input: [('Tom', 70), ('Jerry', 85), ('Spike', 80)]
#             Output:
#             Mean: 78.33
#             Students above mean: [('Jerry', 85)]
#
#          3. Input: [('Emma', 90), ('Liam', 90), ('Olivia', 90)]
#             Output:
#             Mean: 90.0
#             Students above mean: []  (no one is strictly above mean)"
#
# Characteristics:
# - Multiple examples provided (typically 3-5)
# - Shows different scenarios (edge cases, normal cases)
# - Provides more context for pattern recognition
# - Demonstrates edge cases (like equal values)
# ============================================================================

def analyze_marks_few_shot(students_marks):
    """
    Analyze student marks using few-shot approach.
    
    Following the pattern shown in multiple examples:
    - Handle empty lists
    - Calculate mean precisely
    - Use strict comparison (> not >=)
    - Return empty list when no students are above mean
    - Format output consistently
    
    Args:
        students_marks (list): List of tuples (student_name, mark)
    
    Returns:
        dict: Dictionary containing mean (rounded to 2 decimals) and 
              students above mean
    """
    # Handle empty input
    if not students_marks:
        return {"mean": 0.0, "above_mean": []}
    
    # Calculate mean
    marks = [mark for _, mark in students_marks]
    mean = sum(marks) / len(marks)
    
    # Find students strictly above mean (as shown in examples)
    above_mean = [(name, mark) for name, mark in students_marks if mark > mean]
    
    return {
        "mean": round(mean, 2),  # Round for readability, as shown in examples
        "above_mean": above_mean
    }


# ============================================================================
# ENHANCED VERSION: Additional functionality with few-shot learning
# ============================================================================

def analyze_marks_enhanced(students_marks):
    """
    Enhanced analysis with additional statistics (demonstrating few-shot
    with multiple examples showing various features).
    
    Examples showed:
    - Basic mean calculation
    - Filtering above mean
    - Handling edge cases
    - Additional features like sorting by marks
    
    Args:
        students_marks (list): List of tuples (student_name, mark)
    
    Returns:
        dict: Dictionary containing mean, students above mean (sorted),
              total students, and statistics
    """
    if not students_marks:
        return {
            "mean": 0.0,
            "above_mean": [],
            "total_students": 0,
            "min_mark": 0,
            "max_mark": 0
        }
    
    marks = [mark for _, mark in students_marks]
    mean = sum(marks) / len(marks)
    above_mean = [(name, mark) for name, mark in students_marks if mark > mean]
    
    # Sort by marks descending (highest first)
    above_mean_sorted = sorted(above_mean, key=lambda x: x[1], reverse=True)
    
    return {
        "mean": round(mean, 2),
        "above_mean": above_mean_sorted,
        "total_students": len(students_marks),
        "min_mark": min(marks),
        "max_mark": max(marks)
    }


# ============================================================================
# TESTING ALL APPROACHES
# ============================================================================

if __name__ == "__main__":
    # Test data sets
    test_case_1 = [
        ('Alice', 85),
        ('Bob', 90),
        ('Charlie', 75),
        ('Diana', 95)
    ]
    
    test_case_2 = [
        ('Tom', 70),
        ('Jerry', 85),
        ('Spike', 80)
    ]
    
    test_case_3 = [
        ('Emma', 90),
        ('Liam', 90),
        ('Olivia', 90)
    ]
    
    test_case_4 = []  # Edge case: empty list
    
    test_case_5 = [
        ('Student1', 65),
        ('Student2', 72),
        ('Student3', 88),
        ('Student4', 91),
        ('Student5', 78)
    ]
    
    print("=" * 70)
    print("ZERO-SHOT APPROACH RESULTS")
    print("=" * 70)
    print("\nTest Case 1:")
    result1 = analyze_marks_zero_shot(test_case_1)
    print(f"Mean: {result1['mean']}")
    print(f"Students above mean: {result1['above_mean']}")
    
    print("\nTest Case 2:")
    result2 = analyze_marks_zero_shot(test_case_2)
    print(f"Mean: {result2['mean']:.2f}")
    print(f"Students above mean: {result2['above_mean']}")
    
    print("\n" + "=" * 70)
    print("ONE-SHOT APPROACH RESULTS")
    print("=" * 70)
    print("\nTest Case 1 (same as example):")
    result1_oneshot = analyze_marks_one_shot(test_case_1)
    print(f"Mean: {result1_oneshot['mean']}")
    print(f"Students above mean: {result1_oneshot['above_mean']}")
    
    print("\nTest Case 3 (edge case - all equal):")
    result3_oneshot = analyze_marks_one_shot(test_case_3)
    print(f"Mean: {result3_oneshot['mean']}")
    print(f"Students above mean: {result3_oneshot['above_mean']}")
    
    print("\n" + "=" * 70)
    print("FEW-SHOT APPROACH RESULTS")
    print("=" * 70)
    print("\nTest Case 1:")
    result1_fewshot = analyze_marks_few_shot(test_case_1)
    print(f"Mean: {result1_fewshot['mean']}")
    print(f"Students above mean: {result1_fewshot['above_mean']}")
    
    print("\nTest Case 2:")
    result2_fewshot = analyze_marks_few_shot(test_case_2)
    print(f"Mean: {result2_fewshot['mean']}")
    print(f"Students above mean: {result2_fewshot['above_mean']}")
    
    print("\nTest Case 3 (edge case):")
    result3_fewshot = analyze_marks_few_shot(test_case_3)
    print(f"Mean: {result3_fewshot['mean']}")
    print(f"Students above mean: {result3_fewshot['above_mean']}")
    
    print("\nTest Case 4 (empty list):")
    result4_fewshot = analyze_marks_few_shot(test_case_4)
    print(f"Mean: {result4_fewshot['mean']}")
    print(f"Students above mean: {result4_fewshot['above_mean']}")
    
    print("\n" + "=" * 70)
    print("ENHANCED VERSION (Few-shot with more features)")
    print("=" * 70)
    print("\nTest Case 5:")
    result5_enhanced = analyze_marks_enhanced(test_case_5)
    print(f"Total students: {result5_enhanced['total_students']}")
    print(f"Mean: {result5_enhanced['mean']}")
    print(f"Min mark: {result5_enhanced['min_mark']}")
    print(f"Max mark: {result5_enhanced['max_mark']}")
    print(f"Students above mean (sorted): {result5_enhanced['above_mean']}")
    
    print("\n" + "=" * 70)
    print("COMPARISON: All approaches produce same results for same input")
    print("=" * 70)
    print("Test Case 1 - Mean comparison:")
    print(f"  Zero-shot:  {analyze_marks_zero_shot(test_case_1)['mean']}")
    print(f"  One-shot:   {analyze_marks_one_shot(test_case_1)['mean']}")
    print(f"  Few-shot:   {analyze_marks_few_shot(test_case_1)['mean']}")

