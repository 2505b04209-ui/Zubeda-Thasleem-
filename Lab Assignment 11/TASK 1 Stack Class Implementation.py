# =============================================
# LAB 11.3 – TASK 1: Stack Class Implementation
# AI Tool: GROK | Full Size + Comment
# =============================================

# -------------------------------------------------
# STACK CLASS – Clean, Safe, Pythonic
# -------------------------------------------------
class Stack:
    """
    A simple Stack data structure using list.

    Operations:
        - push(item): Add item to top
        - pop(): Remove and return top item
        - peek(): View top item without removing
        - is_empty(): Check if stack is empty
        - size(): Return number of items

    Uses Python list as underlying storage.
    LIFO (Last In, First Out) principle.
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Constructor – Initialize empty stack
    # ------------------------------------------------------------------
    def __init__(self):
        # Internal list to store stack elements
        self.items = []
        print("Stack created! Ready to push items.")

    # ------------------------------------------------------------------
    # STEP 2: Push – Add item to top of stack
    # ------------------------------------------------------------------
    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item (any): Data to push (int, str, etc.)

        Prints confirmation message.
        """
        # Add item to end of list (top of stack)
        self.items.append(item)
        
        # Show what was pushed
        print(f"Pushed: {item} → Stack: {self.items}")

    # ------------------------------------------------------------------
    # STEP 3: Pop – Remove and return top item
    # ------------------------------------------------------------------
    def pop(self):
        """
        Remove and return the top item.

        Returns:
            any: Top item

        Raises:
            IndexError: If stack is empty
        """
        # Check if stack is empty
        if self.is_empty():
            print("Error: Cannot pop from empty stack!")
            return None
        
        # Remove and return last item
        popped = self.items.pop()
        print(f"Popped: {popped} → Stack: {self.items}")
        return popped

    # ------------------------------------------------------------------
    # STEP 4: Peek – View top item without removing
    # ------------------------------------------------------------------
    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            any: Top item or None if empty
        """
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        
        top_item = self.items[-1]
        print(f"Top item (peek): {top_item}")
        return top_item

    # ------------------------------------------------------------------
    # STEP 5: is_empty – Check if stack has no items
    # ------------------------------------------------------------------
    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if empty, False otherwise
        """
        empty = len(self.items) == 0
        if empty:
            print("Stack is EMPTY.")
        return empty

    # ------------------------------------------------------------------
    # STEP 6: size – Return count of items
    # ------------------------------------------------------------------
    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            int: Count of items
        """
        count = len(self.items)
        print(f"Stack size: {count}")
        return count


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – STACK OPERATIONS\n" + "="*60)
    
    # Create a new stack
    s = Stack()

    print("\n1. Push 3 items")
    s.push(10)
    s.push(20)
    s.push(30)
    print()

    print("2. Peek top")
    s.peek()
    print()

    print("3. Pop one item")
    s.pop()
    print()

    print("4. Check size")
    s.size()
    print()

    print("5. Push string & float")
    s.push("Hello")
    s.push(3.14)
    print()

    print("6. Pop all items")
    s.pop()
    s.pop()
    s.pop()
    print()

    print("7. Try pop from empty")
    s.pop()
    print()

    print("8. Final state")
    s.size()
    s.is_empty()