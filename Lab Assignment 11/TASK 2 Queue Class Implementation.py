# =============================================
# LAB 11.3 – TASK 2: Queue Class Implementation
# AI Tool: GROK | Full Size + Elaborated Comments + 8 Examples
# =============================================

# -------------------------------------------------
# QUEUE CLASS – FIFO (First In, First Out)
# -------------------------------------------------
class Queue:
    """
    A simple Queue data structure using Python list.

    Operations:
        - enqueue(item): Add item to rear (end)
        - dequeue(): Remove and return front item
        - peek(): View front item without removing
        - is_empty(): Check if queue is empty
        - size(): Return number of items

    FIFO Principle: First In, First Out
    Like a line at a ticket counter.
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Constructor – Initialize empty queue
    # ------------------------------------------------------------------
    def __init__(self):
        """
        Create a new empty queue.
        """
        # Internal list to store queue elements
        # Index 0 = front, last index = rear
        self.items = []
        
        # Welcome message
        print("Queue created! Ready to enqueue items.")

    # ------------------------------------------------------------------
    # STEP 2: Enqueue – Add item to rear (end of list)
    # ------------------------------------------------------------------
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item (any): Data to add (int, str, float, etc.)

        Prints confirmation with current queue state.
        """
        # Add item to the end of the list
        self.items.append(item)
        
        # Show updated queue
        print(f"Enqueued: {item} → Queue: {self.items}")

    # ------------------------------------------------------------------
    # STEP 3: Dequeue – Remove and return front item (index 0)
    # ------------------------------------------------------------------
    def dequeue(self):
        """
        Remove and return the front item.

        Returns:
            any: Front item or None if empty

        Raises:
            IndexError: If queue is empty
        """
        # Check if queue is empty
        if self.is_empty():
            print("Error: Cannot dequeue from empty queue!")
            return None
        
        # Remove and return first item (index 0)
        front_item = self.items.pop(0)
        print(f"Dequeued: {front_item} → Queue: {self.items}")
        return front_item

    # ------------------------------------------------------------------
    # STEP 4: Peek – View front item without removing
    # ------------------------------------------------------------------
    def peek(self):
        """
        Return the front item without removing it.

        Returns:
            any: Front item or None if empty
        """
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        
        front = self.items[0]
        print(f"Front item (peek): {front}")
        return front

    # ------------------------------------------------------------------
    # STEP 5: is_empty – Check if no items in queue
    # ------------------------------------------------------------------
    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if empty, False otherwise
        """
        empty = len(self.items) == 0
        if empty:
            print("Queue is EMPTY.")
        return empty

    # ------------------------------------------------------------------
    # STEP 6: size – Return count of items
    # ------------------------------------------------------------------
    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            int: Count of items
        """
        count = len(self.items)
        print(f"Queue size: {count}")
        return count


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – QUEUE OPERATIONS\n" + "="*70)
    
    # Create a new queue
    q = Queue()

    print("\n1. Enqueue 3 items")
    q.enqueue("Ticket A")
    q.enqueue("Ticket B")
    q.enqueue("Ticket C")
    print()

    print("2. Peek front")
    q.peek()
    print()

    print("3. Dequeue one item")
    q.dequeue()
    print()

    print("4. Check size")
    q.size()
    print()

    print("5. Enqueue numbers & float")
    q.enqueue(100)
    q.enqueue(3.14)
    print()

    print("6. Dequeue all items")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print()

    print("7. Try dequeue from empty")
    q.dequeue()
    print()

    print("8. Final state")
    q.size()
    q.is_empty()