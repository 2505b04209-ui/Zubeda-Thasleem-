# =============================================
#  TASK 5: DATE FORMAT CONVERTER – TDD WITH FLAIR!
#  AI: GROK (Your Final Boss Copilot!)
#  TDD: Test First → Code → Victory Lap!
# =============================================

import unittest
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

# =============================================
#  STEP 1: AI-GENERATED TEST CASES (GROK!)
# =============================================
class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_leap_year(self):
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")

    def test_new_year(self):
        self.assertEqual(convert_date_format("2025-01-01"), "01-01-2025")

    def test_end_of_month(self):
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")

    def test_invalid_format(self):
        self.assertEqual(convert_date_format("15/10/2023"), "Invalid")
        self.assertEqual(convert_date_format("2023-10-15-00"), "Invalid")

    def test_invalid_date(self):
        self.assertEqual(convert_date_format("2023-13-45"), "Invalid")
        self.assertEqual(convert_date_format("2023-04-31"), "Invalid")  # April has 30

    def test_string_input(self):
        self.assertEqual(convert_date_format("hello"), "Invalid")


# =============================================
#  STEP 2: THE DATE WIZARD!
# =============================================
def convert_date_format(date_str):
    """
    Convert "YYYY-MM-DD" → "DD-MM-YYYY"
    Returns "Invalid" if format or date is wrong
    """
    if not isinstance(date_str, str) or len(date_str) != 10:
        return "Invalid"
    
    try:
        # Parse input
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        # Format output
        return dt.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid"


# =============================================
#  FUN & COLORFUL TEST RUNNER
# =============================================
def run_with_style():
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "═" * 68)
    print(Fore.CYAN + Style.BRIGHT + "  DATE FORMAT CONVERTER – TDD FINAL BOSS!")
    print(Fore.YELLOW + "═" * 68 + "\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(TestConvertDateFormat)
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(Fore.YELLOW + "\n" + "═" * 68)
    if result.wasSuccessful():
        print(Fore.GREEN + Style.BRIGHT + "  TIME TRAVEL SUCCESS! ALL TESTS PASSED!")
        print(Fore.MAGENTA + f"  Total Tests: {result.testsRun}")
    else:
        print(Fore.RED + "  Time paradox! Fix it!")
    print(Fore.YELLOW + "═" * 68 + "\n")


# =============================================
#  LIVE DEMO (Time Machine!)
# =============================================
def demo():
    print(Fore.BLUE + Style.BRIGHT + "  TIME MACHINE DEMO:")
    dates = [
        "2023-10-15",
        "2024-02-29",
        "2023-13-45",
        "hello"
    ]
    for d in dates:
        result = convert_date_format(d)
        color = Fore.GREEN if result != "Invalid" else Fore.RED
        print(f"  {d} → {color}{result}{Style.RESET_ALL}")
    print()


# =============================================
#  RUN EVERYTHING!
# =============================================
if __name__ == '__main__':
    demo()
    run_with_style()