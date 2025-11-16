# =============================================
# LAB 11.3 – TASK 3: Singly Linked List Implementation
# AI Tool: GROK | Full Size + Elaborated Comments + 8 Examples
# =============================================

# -------------------------------------------------
# NODE CLASS – Building block of Linked List
# -------------------------------------------------
class Node:
    """
    A single node in a singly linked list.

    Attributes:
        data (any): Value stored in node
        next (Node): Reference to next node (None if last)
    """
    
    # ------------------------------------------------------------------
    # Constructor: Create node with data and next pointer
    # ------------------------------------------------------------------
    def __init__(self, data):
        """
        Initialize node with data.
        
        Args:
            data (any): Value to store (int, str, etc.)
        """
        self.data = data        # Store the value
        self.next = None        # Next pointer initially None
        print(f"Node created with data: {data}")


# -------------------------------------------------
# LINKED LIST CLASS – Main structure
# -------------------------------------------------
class LinkedList:
    """
    Singly Linked List with basic operations.

    Operations:
        - insert_at_end(data): Add node at end
        - insert_at_beginning(data): Add node at start
        - display(): Print all nodes in order
        - is_empty(): Check if list is empty
        - size(): Count total nodes

    Structure: head → node → node → ... → None
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Constructor – Initialize empty list
    # ------------------------------------------------------------------
    def __init__(self):
        """
        Create a new empty linked list.
        """
        self.head = None  # Head points to first node
        print("Linked List created! Head = None")

    # ------------------------------------------------------------------
    # STEP 2: Insert at End – Add node to tail
    # ------------------------------------------------------------------
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Args:
            data (any): Value for new node
        """
        # Create new node
        new_node = Node(data)
        
        # Case 1: Empty list → new node becomes head
        if self.is_empty():
            self.head = new_node
            print(f"Inserted at end (first node): {data}")
            return
        
        # Case 2: Traverse to last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Link new node to last node
        current.next = new_node
        print(f"Inserted at end: {data}")

    # ------------------------------------------------------------------
    # STEP 3: Insert at Beginning – Add node to head
    # ------------------------------------------------------------------
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.

        Args:
            data (any): Value for new node
        """
        # Create new node
        new_node = Node(data)
        
        # Point new node to current head
        new_node.next = self.head
        
        # Update head to new node
        self.head = new_node
        print(f"Inserted at beginning: {data}")

    # ------------------------------------------------------------------
    # STEP 4: Display – Print entire list
    # ------------------------------------------------------------------
    def display(self):
        """
        Print all nodes in the linked list.

        Format: [data] -> [data] -> ... -> None
        """
        if self.is_empty():
            print("List is EMPTY! Nothing to display.")
            return
        
        print("Linked List: ", end="")
        current = self.head
        while current is not None:
            print(f"[{current.data}]", end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print(" -> None")
    
    # ------------------------------------------------------------------
    # STEP 5: is_empty – Check if no nodes
    # ------------------------------------------------------------------
    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            bool: True if empty
        """
        empty = self.head is None
        if empty:
            print("List is EMPTY.")
        return empty
    # ------------------------------------------------------------------
    # STEP 6: size – Count total nodes
    # ------------------------------------------------------------------
    def size(self):
        """
        Count total number of nodes.

        Returns:
            int: Number of nodes
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(f"List size: {count}")
        return count
# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – LINKED LIST OPERATIONS\n" + "="*70)
    
    # Create a new linked list
    ll = LinkedList()
    print("\n1. Insert 3 nodes at end")
    ll.insert_at_end("Apple")
    ll.insert_at_end("Banana")
    ll.insert_at_end("Cherry")
    ll.display()
    print()

    print("2. Insert at beginning")
    ll.insert_at_beginning("Mango")
    ll.display()
    print()

    print("3. Insert mixed types")
    ll.insert_at_end(100)
    ll.insert_at_end(3.14)
    ll.display()
    print()
    print("4. Check size")
    ll.size()
    print()

    print("5. Insert more at beginning")
    ll.insert_at_beginning("First")
    ll.display()
    print()
    print("6. Empty list test")
    empty_ll = LinkedList()
    empty_ll.display()
    empty_ll.is_empty()
    print()
    print("7. Single node")
    single = LinkedList()
    single.insert_at_end("OnlyOne")
    single.display()
    print()

    print("8. Final state of main list")
    ll.display()
    ll.size()