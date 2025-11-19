# =============================================
# LAB 12.3 – TASK 1: LINEAR SEARCH IMPLEMENTATION
# Objective: Find index of target in list
# AI Tool: GitHub Copilot
# =============================================

def linear_search(arr, target):
    """
    Search for target in list and return its index.
    
    Linear search: Check each element from start to end.
    Time Complexity: O(n) – worst case checks all elements.
    Space Complexity: O(1) – no extra space used.
    
    Args:
        arr (list): List to search in
        target (any): Value to find
    
    Returns:
        int: Index if found, -1 if not found
    """
    
    # Step 0: Input validation (optional but safe)
    if not isinstance(arr, list):
        print("Error: 'arr' must be a list")
        return -1
    
    if len(arr) == 0:
        print("Error: Empty list – nothing to search")
        return -1
    
    # Step 1: Loop through list with index
    # range(len(arr)) gives 0, 1, 2, ..., len(arr)-1
    for i in range(len(arr)):  # i = index (0 to n-1)
        
        # Step 2: Check if current element matches target
        if arr[i] == target:  # Compare arr[index] with target
        
            # Step 3: Found it! Print and return index
            print(f"✓ Found '{target}' at index {i}")
            return i  # Return immediately – early exit
    
    # Step 4: Loop completed without match
    print(f"✗ '{target}' not found in list")
    return -1  # Convention: -1 means "not found"


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    # Test list
    test_list = [10, 23, 45, 70, 11, 15, 88, 23]
    
    print("8 EXAMPLES – LINEAR SEARCH\n" + "="*50)
    
    # Example 1: Find first occurrence
    print("\n1. Find first '23'")
    index = linear_search(test_list, 23)
    print(f"   → Index: {index}")
    
    # Example 2: Find last element
    print("\n2. Find '88' (last)")
    index = linear_search(test_list, 88)
    print(f"   → Index: {index}")
    
    # Example 3: Find first element
    print("\n3. Find '10' (first)")
    index = linear_search(test_list, 10)
    print(f"   → Index: {index}")
    
    # Example 4: Not in list
    print("\n4. Find '99' (not in list)")
    index = linear_search(test_list, 99)
    print(f"   → Index: {index}")
    
    # Example 5: Middle element
    print("\n5. Find '45' (middle)")
    index = linear_search(test_list, 45)
    print(f"   → Index: {index}")
    
    # Example 6: After target (15 after 11)
    print("\n6. Find '15'")
    index = linear_search(test_list, 15)
    print(f"   → Index: {index}")
    
    # Example 7: Duplicate (second 23)
    print("\n7. Find second '23'")
    index = linear_search(test_list, 23)
    print(f"   → Index: {index} (first occurrence)")
    
    # Example 8: Empty list
    print("\n8. Empty list")
    empty = []
    index = linear_search(empty, 100)
    print(f"   → Index: {index}")