# =============================================
# LAB 10.3 – TASK 4: Modularize Long Function
# AI Tool:  | Before → After → 8 Examples
# =============================================

# -------------------------------------------------
# ORIGINAL CODE (Monolithic )
# -------------------------------------------------
"""
def process_scores(scores):
    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)

    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s

    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
"""

# -------------------------------------------------
# MODULARIZED CODE (Clean + Helpers)
# -------------------------------------------------
def calculate_average(scores):
    """
    Calculate average of scores.

    Args:
        scores (list): List of numeric values

    Returns:
        float: Average value

    Raises:
        ValueError: If list is empty
        TypeError: If non-numeric values
    """
    if not scores:
        raise ValueError("Cannot calculate average of empty list")
    
    total = sum(scores)
    return total / len(scores)


def find_highest(scores):
    """
    Find highest score.

    Args:
        scores (list): List of comparable values

    Returns:
        any: Maximum value

    Raises:
        ValueError: If list is empty
    """
    if not scores:
        raise ValueError("List cannot be empty")
    return max(scores)


def find_lowest(scores):
    """
    Find lowest score.

    Args:
        scores (list): List of comparable values

    Returns:
        any: Minimum value

    Raises:
        ValueError: If list is empty
    """
    if not scores:
        raise ValueError("List cannot be empty")
    return min(scores)

def process_scores(scores):
    """
    Process list of scores and print stats.

    Uses helper functions for clean, reusable logic.

    Args:
        scores (list): List of numbers

    Prints:
        Average, Highest, Lowest
    """
    try:
        # Validate input
        if not isinstance(scores, list):
            raise TypeError("Input must be a list")
        
        # Use helper functions
        avg = calculate_average(scores)
        high = find_highest(scores)
        low = find_lowest(scores)
        
        # Print formatted output
        print("=" * 40)
        print("   SCORE ANALYSIS REPORT   ")
        print("=" * 40)
        print(f"Average : {avg:,.2f}")
        print(f"Highest : {high}")
        print(f"Lowest  : {low}")
        print("=" * 40)
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
# =============================================
#  TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – MODULAR SCORE PROCESSOR\n" + "="*60)
    
    tests = [
        [85, 90, 78, 92, 88],                    # Normal
        [100],                                  # Single
        [],                                     # Empty
        [70, 70, 70],                           # All same
        [-5, 0, 5],                             # Negative
        [95.5, 88.7, 76.3],                     # Float
        ["90", 85, 88],                         # Mixed types
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Large
    ]
    for i, data in enumerate(tests, 1):
        print(f"\n{i}. Input: {data}")
        process_scores(data)