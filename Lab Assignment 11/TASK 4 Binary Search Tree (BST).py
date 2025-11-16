# =============================================
# LAB 11.3 – TASK 4: Binary Search Tree (BST)
# AI Tool: GROK | Full Size + Elaborated Comments + 8 Examples
# =============================================

# -------------------------------------------------
# NODE CLASS – Building block of BST
# -------------------------------------------------
class TreeNode:
    """
    A single node in a Binary Search Tree.

    Attributes:
        data (int): Value stored in node
        left (TreeNode): Left child (smaller values)
        right (TreeNode): Right child (larger values)
    """
    
    # ------------------------------------------------------------------
    # Constructor: Create node with data
    # ------------------------------------------------------------------
    def __init__(self, data):
        """
        Initialize node with data and None children.
        
        Args:
            data (int): Integer value for BST
        """
        self.data = data          # Store the value
        self.left = None          # Left child (values < data)
        self.right = None         # Right child (values > data)
        print(f"Node created: {data}")


# -------------------------------------------------
# BST CLASS – Main structure with insert & inorder
# -------------------------------------------------
class BinarySearchTree:
    """
    Binary Search Tree with insert and inorder traversal.

    Properties:
        - Left < Root < Right
        - No duplicates
        - O(log n) average insert/search

    Operations:
        - insert(data): Add node in correct position
        - inorder_traversal(): Print sorted order (Left → Root → Right)
        - display_tree(): Visual tree structure
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Constructor – Initialize empty BST
    # ------------------------------------------------------------------
    def __init__(self):
        """
        Create a new empty BST.
        """
        self.root = None  # Root of the tree
        print("BST created! Root = None")

    # ------------------------------------------------------------------
    # STEP 2: Insert – Add node in correct position
    # ------------------------------------------------------------------
    def insert(self, data):
        """
        Insert a value into the BST maintaining order.

        Args:
            data (int): Value to insert
        """
        # Create new node
        new_node = TreeNode(data)
        
        # Case 1: Empty tree → new node is root
        if self.root is None:
            self.root = new_node
            print(f"Inserted as ROOT: {data}")
            return
        
        # Case 2: Traverse to find correct position
        current = self.root
        while True:
            if data < current.data:
                # Go left
                if current.left is None:
                    current.left = new_node
                    print(f"Inserted LEFT of {current.data}: {data}")
                    break
                current = current.left
            elif data > current.data:
                # Go right
                if current.right is None:
                    current.right = new_node
                    print(f"Inserted RIGHT of {current.data}: {data}")
                    break
                current = current.right
            else:
                # Duplicate → ignore
                print(f"Duplicate {data} ignored (BST allows unique values)")
                break

    # ------------------------------------------------------------------
    # STEP 3: Inorder Traversal – Left → Root → Right (Sorted)
    # ------------------------------------------------------------------
    def inorder_traversal(self):
        """
        Print nodes in sorted (ascending) order.
        """
        print("Inorder Traversal (Sorted): ", end="")
        self._inorder_helper(self.root)
        print()  # New line

    def _inorder_helper(self, node):
        """
        Recursive helper for inorder traversal.
        """
        if node is not None:
            self._inorder_helper(node.left)
            print(node.data, end=" ")
            self._inorder_helper(node.right)

    # ------------------------------------------------------------------
    # STEP 4: Display Tree – Visual structure
    # ------------------------------------------------------------------
    def display_tree(self):
        """
        Print tree structure with indentation.
        """
        print("BST Structure:")
        self._display_helper(self.root, 0)

    def _display_helper(self, node, level):
        """
        Recursive helper to print tree with levels.
        """
        if node is None:
            return
        self._display_helper(node.right, level + 1)
        print("    " * level + f"└─ {node.data}")
        self._display_helper(node.left, level + 1)


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – BINARY SEARCH TREE\n" + "="*70)
    
    # Create BST
    bst = BinarySearchTree()

    print("\n1. Insert root and basic nodes")
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.display_tree()
    print()

    print("2. Insert more nodes")
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.display_tree()
    print()

    print("3. Inorder traversal (should be sorted)")
    bst.inorder_traversal()
    print()

    print("4. Try duplicate")
    bst.insert(40)
    print()

    print("5. Insert extreme values")
    bst.insert(10)
    bst.insert(90)
    bst.display_tree()
    print()

    print("6. Empty BST test")
    empty_bst = BinarySearchTree()
    empty_bst.inorder_traversal()
    print()

    print("7. Single node BST")
    single = BinarySearchTree()
    single.insert(100)
    single.display_tree()
    single.inorder_traversal()
    print()

    print("8. Final BST state")
    bst.display_tree()
    bst.inorder_traversal()