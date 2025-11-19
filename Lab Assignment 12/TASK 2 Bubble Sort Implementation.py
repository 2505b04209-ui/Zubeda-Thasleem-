# =============================================
# LAB 12.3 – TASK 2: BUBBLE SORT IMPLEMENTATION
# AI Tool: GitHub Copilot / Grok
# Every single line explained
# =============================================

def bubble_sort(arr):
    """
    Sort a list in ascending order using Bubble Sort algorithm.
    
    How it works:
    - Repeatedly step through the list
    - Compare adjacent elements
    - Swap if they are in wrong order
    - Largest element "bubbles up" to the end in each pass
    
    Time Complexity : O(n²) worst & average, O(n) best (already sorted)
    Space Complexity: O(1) – in-place sorting
    """
    
    # Step 1: Get length of list
    n = len(arr)
    
    # Step 2: If list has 0 or 1 element → already sorted
    if n <= 1:
        print("List has 0 or 1 element → Already sorted!")
        return arr
    
    print(f"Original list : {arr}")
    print(f"Starting Bubble Sort on {n} elements...\n")
    
    # Step 3: Outer loop – one pass for each element (except last)
    # After i-th pass, last i elements are in correct position
    for i in range(n):
        
        # Step 4: Flag to detect if any swap happened in this pass
        # Helps optimize: if no swap → list is sorted
        swapped = False
        
        print(f"Pass {i+1}:")
        
        # Step 5: Inner loop – compare adjacent elements
        # We only go till (n-i-1) because last i elements are already sorted
        for j in range(0, n - i - 1):
            
            # Step 6: Compare current and next element
            print(f"   Comparing {arr[j]} and {arr[j+1]}", end=" ")
            
            if arr[j] > arr[j+1]:
                # Step 7: Swap if left > right
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"→ SWAPPED → {arr}")
            else:
                print(f"→ No swap → {arr}")
        
        # Step 8: If no swapping happened → list is fully sorted
        if not swapped:
            print(f"No swaps in pass {i+1} → List is now SORTED!")
            break
        
        # Optional: Show list after each pass
        print(f"   After pass {i+1}: {arr}\n")
    
    print("Bubble Sort completed!")
    return arr


# =============================================
# 8 TEST EXAMPLES (Run to see full process)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – BUBBLE SORT\n" + "="*70)
    
    # Example 1: Random list
    print("\n1. Random list")
    lst1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(lst1.copy())
    
    # Example 2: Already sorted
    print("\n2. Already sorted (Best case – early exit)")
    lst2 = [10, 20, 30, 40, 50]
    bubble_sort(lst2.copy())
    
    # Example 3: Reverse sorted
    print("\n3. Reverse sorted (Worst case)")
    lst3 = [99, 77, 55, 33, 11]
    bubble_sort(lst3.copy())
    
    # Example 4: With duplicates
    print("\n4. With duplicates")
    lst4 = [5, 2, 8, 2, 9, 1]
    bubble_sort(lst4.copy())
    
    # Example 5: Single element
    print("\n5. Single element")
    bubble_sort([42])
    
    # Example 6: Empty list
    print("\n6. Empty list")
    bubble_sort([])
    
    # Example 7: Floating point
    print("\n7. Floating point numbers")
    lst7 = [3.14, 1.1, 5.5, 2.2, 4.4]
    bubble_sort(lst7.copy())
    
    # Example 8: Strings (lexicographical order)
    print("\n8. List of strings")
    lst8 = ["mango", "apple", "cherry", "banana"]
    bubble_sort(lst8.copy())