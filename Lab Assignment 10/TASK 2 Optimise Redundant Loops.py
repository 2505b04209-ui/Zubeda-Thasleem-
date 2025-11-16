# =============================================
# LAB 10.3 – TASK 2: Optimize Redundant Loops
# AI Tool: GROK | Before → After → 8 Examples
# =============================================

# -------------------------------------------------
# ORIGINAL CODE (O(n²) – Slow & Messy)
# -------------------------------------------------
"""
def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res
"""

# -------------------------------------------------
# OPTIMIZED CODE (O(n) – Fast + Sets)
# -------------------------------------------------
def find_common(a, b):
    """
    Find common elements between two lists.

    Uses set intersection for optimal performance.
    Handles duplicates by returning unique elements.

    Args:
        a (list): First list
        b (list): Second list

    Returns:
        set: Common elements (no duplicates)

    Examples:
        See 8 test cases below
    """
    # Input validation
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")
    
    # Use set intersection → O(n + m)
    return set(a) & set(b)


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – FIND COMMON ELEMENTS\n" + "="*50)
    
    tests = [
        ([1, 2, 3, 4], [3, 4, 5, 6], {3, 4}),
        ([1, 1, 2, 2], [2, 2, 3], {2}),
        ([], [1, 2], set()),
        ([1, 2], [], set()),
        (["a", "b", "c"], ["b", "c", "d"], {"b", "c"}),
        ([1, 2, 3], [1, 2, 3], {1, 2, 3}),
        (["x"], ["x"], {"x"}),
        ([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 8], {5, 6, 7, 8}),
    ]

    for i, (list1, list2, expected) in enumerate(tests, 1):
        result = find_common(list1, list2)
        status = "PASS" if result == expected else "FAIL"
        print(f"{i}. List A: {list1}")
        print(f"    List B: {list2}")
        print(f"    Common: {sorted(result)} | Expected: {sorted(expected)} → {status}\n")