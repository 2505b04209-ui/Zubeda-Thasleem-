# =============================================
#  TASK 3: SENTENCE PALINDROME – TDD WITH STYLE!
#  AI: GROK (Your Smart Copilot!)
#  TDD: Test First → Code → Celebrate!
# =============================================

import unittest
from colorama import init, Fore, Style
import re

init(autoreset=True)

# =============================================
#  STEP 1: AI-GENERATED TEST CASES (GROK!)
# =============================================
class TestIsSentencePalindrome(unittest.TestCase):
    """
    GROK-generated test cases for is_sentence_palindrome()
    Ignores: case, spaces, punctuation
    """

    def test_classic_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))

    def test_racecar(self):
        self.assertTrue(is_sentence_palindrome("Racecar"))

    def test_mixed_case_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Madam, in Eden, I'm Adam!"))

    def test_not_palindrome(self):
        self.assertFalse(is_sentence_palindrome("Hello World"))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))  # Empty is palindrome

    def test_single_word(self):
        self.assertTrue(is_sentence_palindrome("Noon"))

    def test_with_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_invalid_input(self):
        self.assertFalse(is_sentence_palindrome(None))  # Should handle None


# =============================================
#  STEP 2: THE PALINDROME DETECTOR!
# =============================================
def is_sentence_palindrome(sentence):
    """
    Check if sentence is palindrome.
    Steps:
        1. Convert to lowercase
        2. Remove non-alphanumeric
        3. Compare with reverse
    """
    if sentence is None:
        return False

    # Step 1: Normalize
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence.lower())
    
    # Step 2: Check palindrome
    return cleaned == cleaned[::-1]


# =============================================
#  FUN & COLORFUL TEST RUNNER
# =============================================
def run_with_style():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "═" * 65)
    print(Fore.CYAN + Style.BRIGHT + "  SENTENCE PALINDROME – TDD IN ACTION!")
    print(Fore.MAGENTA + "═" * 65 + "\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(TestIsSentencePalindrome)
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(Fore.MAGENTA + "\n" + "═" * 65)
    if result.wasSuccessful():
        print(Fore.GREEN + Style.BRIGHT + "  ALL PALINDROMES DETECTED! YOU'RE A TDD MASTER!")
        print(Fore.YELLOW + f"  Total Tests: {result.testsRun}")
    else:
        print(Fore.RED + "  Some failed. Try again!")
    print(Fore.MAGENTA + "═" * 65 + "\n")


# =============================================
#  QUICK DEMO (Fun Examples!)
# =============================================
def demo():
    print(Fore.BLUE + Style.BRIGHT + "  QUICK PALINDROME DEMO:")
    examples = [
        "A man a plan a canal Panama",
        "Racecar",
        "Hello World",
        "Madam, in Eden, I'm Adam!"
    ]
    for ex in examples:
        result = is_sentence_palindrome(ex)
        color = Fore.GREEN if result else Fore.RED
        print(f"  '{ex}' → {color}{result}{Style.RESET_ALL}")
    print()


# =============================================
#  RUN EVERYTHING!
# =============================================
if __name__ == '__main__':
    demo()
    run_with_style()