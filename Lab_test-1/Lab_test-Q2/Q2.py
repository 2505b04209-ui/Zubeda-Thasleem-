"""Queue class for M.Tech lab with  error messaging and scenario tests."""

from typing import Any, List


class Queue:
    """FIFO queue supporting safe front operations and simple introspection."""

    def __init__(self) -> None:
        """Initialize the queue with an empty list."""
        self.items: List[Any] = []

    def enqueue(self, item: Any) -> str:
        """
        Add an item to the rear of the queue.

        Returns:
            Confirmation string indicating the item was enqueued.
        """
        self.items.append(item)
        return f"Enqueued {item} at rear."

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        Returns:
            The front element, or a Hindi-English error message if empty.
        """
        if self.is_empty():
            return "Error: Queue khali hai boss!"
        return self.items.pop(0)

    def peek(self) -> Any:
        """
        View the front item without removing it.

        Returns:
            The front element, or a Hindi-English error message if empty.
        """
        if self.is_empty():
            return "Error: Queue khali hai boss!"
        return self.items[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no items, otherwise False."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items currently stored."""
        return len(self.items)

    def display(self) -> List[Any]:
        """Return a copy of the current queue state."""
        return list(self.items)


def run_scenarios() -> None:
    """Execute the eight required test scenarios and print their outcomes."""
    q = Queue()

    print("Scenario 1: Dequeue & peek on empty queue")
    print("Dequeue:", q.dequeue())
    print("Peek   :", q.peek())

    print("\nScenario 2: Enqueue 1 to 10")
    for value in range(1, 11):
        print(q.enqueue(value))
    print("Queue state:", q.display())

    print("\nScenario 3: Peek front")
    print("Peek   :", q.peek())

    print("\nScenario 4: Dequeue 5 items")
    for _ in range(5):
        print("Dequeued:", q.dequeue())
    print("Queue state:", q.display())

    print("\nScenario 5: Enqueue 99 and 100, then peek")
    print(q.enqueue(99))
    print(q.enqueue(100))
    print("Peek   :", q.peek())
    print("Queue state:", q.display())

    print("\nScenario 6: Dequeue everything")
    while not q.is_empty():
        print("Dequeued:", q.dequeue())
    print("Queue state:", q.display())

    print("\nScenario 7: Again try dequeue & peek (empty checks)")
    print("Dequeue:", q.dequeue())
    print("Peek   :", q.peek())

    print("\nScenario 8: Enqueue strings 'A','B','C' and show size")
    print(q.enqueue("A"))
    print(q.enqueue("B"))
    print(q.enqueue("C"))
    print("Queue state:", q.display())
    print("Size   :", q.size())


if __name__ == "__main__":
    run_scenarios()


