# =============================================
#  TASK 4: SHOPPING CART CLASS – TDD WITH FLAIR!
#  AI: GROK (Your Ultimate Copilot!)
#  TDD: Test First → Code → Victory!
# =============================================

import unittest
from colorama import init, Fore, Style
init(autoreset=True)

# =============================================
#  STEP 1: AI-GENERATED TEST CASES (GROK!)
# =============================================
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Create fresh cart before each test"""
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("Apple", 50.0)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_cost(), 50.0)

    def test_add_multiple_items(self):
        self.cart.add_item("Banana", 30.0)
        self.cart.add_item("Orange", 40.0)
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.total_cost(), 70.0)

    def test_remove_existing_item(self):
        self.cart.add_item("Mango", 60.0)
        self.cart.remove_item("Mango")
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_remove_nonexistent_item(self):
        self.cart.add_item("Grape", 80.0)
        self.cart.remove_item("Pineapple")
        self.assertEqual(len(self.cart.items), 1)

    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_negative_price_handling(self):
        self.cart.add_item("Cherry", -10.0)
        self.assertEqual(self.cart.total_cost(), 0.0)  # Invalid price ignored

    def test_case_insensitive_remove(self):
        self.cart.add_item("apple", 50.0)
        self.cart.remove_item("APPLE")
        self.assertEqual(len(self.cart.items), 0)


# =============================================
#  STEP 2: THE SHOPPING CART CLASS!
# =============================================
class ShoppingCart:
    """
    A smart shopping cart that:
    - Adds items (name, price)
    - Removes items
    - Calculates total cost
    - Handles errors gracefully
    """
    def __init__(self):
        self.items = {}  # name: price

    def add_item(self, name, price):
        """
        Add item if price >= 0
        """
        if not isinstance(price, (int, float)) or price < 0:
            print(Fore.YELLOW + f"  Invalid price for {name}. Ignored.")
            return
        self.items[name.lower()] = price
        print(Fore.GREEN + f"  Added: {name} → ₹{price:.2f}")

    def remove_item(self, name):
        """
        Remove item (case-insensitive)
        """
        key = name.lower()
        if key in self.items:
            removed_price = self.items.pop(key)
            print(Fore.RED + f"  Removed: {name} (₹{removed_price:.2f})")
        else:
            print(Fore.YELLOW + f"  Not found: {name}")

    def total_cost(self):
        """
        Return total price
        """
        return sum(self.items.values())


# =============================================
#  FUN & COLORFUL TEST RUNNER
# =============================================
def run_with_style():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 70)
    print(Fore.MAGENTA + Style.BRIGHT + "  SHOPPING CART – TDD IN ACTION!")
    print(Fore.CYAN + "═" * 70 + "\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(TestShoppingCart)
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(Fore.CYAN + "\n" + "═" * 70)
    if result.wasSuccessful():
        print(Fore.GREEN + Style.BRIGHT + "  CART SECURED! ALL TESTS PASSED!")
        print(Fore.YELLOW + f"  Total Tests: {result.testsRun}")
    else:
        print(Fore.RED + "  Cart leaked! Fix it!")
    print(Fore.CYAN + "═" * 70 + "\n")


# =============================================
#  LIVE DEMO (Fun Shopping!)
# =============================================
def demo():
    print(Fore.BLUE + Style.BRIGHT + "  LIVE SHOPPING DEMO:")
    cart = ShoppingCart()
    cart.add_item("Laptop", 50000)
    cart.add_item("Mouse", 500)
    cart.add_item("Banana", -10)  # Invalid
    cart.remove_item("MOUSE")
    cart.remove_item("Keyboard")
    print(Fore.CYAN + f"  Final Total: ₹{cart.total_cost():,.2f}")
    print()


# =============================================
#  RUN EVERYTHING!
# =============================================
if __name__ == '__main__':
    demo()
    run_with_style()