# =============================================
#  TASK 2: GRADE ASSIGNMENT – TDD WITH STYLE!
#  TDD: Test First → Code → Celebrate!
# =============================================
import unittest
from colorama import init, Fore, Style
init(autoreset=True)  # Auto-reset colors

# =============================================
#  STEP 1: AI-GENERATED TEST CASES (GROK!)
# =============================================
class TestAssignGrade(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(90), "A")

    def test_grade_B(self):
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(80), "B")

    def test_grade_C(self):
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(70), "C")

    def test_grade_D(self):
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(60), "D")

    def test_grade_F(self):
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(0), "F")

    def test_invalid(self):
        self.assertEqual(assign_grade(-5), "Invalid")
        self.assertEqual(assign_grade(105), "Invalid")
        self.assertEqual(assign_grade("eighty"), "Invalid")


# =============================================
#  STEP 2: THE GRADE MACHINE!
# =============================================
def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid"
    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"


# =============================================
#  FUN & COLORFUL TEST RUNNER
# =============================================
def run_with_style():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "  GRADE ASSIGNMENT – TDD IN ACTION!")
    print(Fore.CYAN + "═" * 60 + "\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(TestAssignGrade)
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(Fore.CYAN + "\n" + "═" * 60)
    if result.wasSuccessful():
        print(Fore.GREEN + Style.BRIGHT + "  ALL TESTS PASSED! YOU'RE A TDD CHAMP!")
        print(Fore.MAGENTA + "  Total Tests: " + str(result.testsRun))
    else:
        print(Fore.RED + "  Some tests failed. Keep coding!")
    print(Fore.CYAN + "═" * 60 + "\n")


# =============================================
#  QUICK DEMO (Optional)
# =============================================
def demo():
    print(Fore.BLUE + "  QUICK DEMO:")
    print(f"  95  → {Fore.GREEN}{assign_grade(95)}{Style.RESET_ALL}")
    print(f"  82  → {Fore.YELLOW}{assign_grade(82)}{Style.RESET_ALL}")
    print(f"  -5  → {Fore.RED}{assign_grade(-5)}{Style.RESET_ALL}")
    print()


# =============================================
#  RUN EVERYTHING!
# =============================================
if __name__ == '__main__':
    demo()
    run_with_style()