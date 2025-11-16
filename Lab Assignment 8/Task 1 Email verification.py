# =============================================
# TASK 1: EMAIL VALIDATOR – TDD with AI
# AI Tool: GitHub Copilot (VS Code)
# =============================================

import unittest
import re

# =============================================
# STEP 1: AI-GENERATED TEST CASES (First!)
# =============================================
class TestIsValidEmail(unittest.TestCase):
    """
    AI-generated test cases for is_valid_email(email)
    Requirements:
        - Must have @ and .
        - Not start/end with special chars
        - Only one @
    """

    def test_valid_emails(self):
        """Test valid email formats"""
        valid = [
            "user@example.com",
            "a@b.co",
            "john.doe123@domain.org",
            "test+filter@mail.com"
        ]
        for email in valid:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_no_at(self):
        """Missing @"""
        self.assertFalse(is_valid_email("userexample.com"))

    def test_invalid_no_dot(self):
        """Missing ."""
        self.assertFalse(is_valid_email("user@domain"))

    def test_invalid_multiple_at(self):
        """Multiple @"""
        self.assertFalse(is_valid_email("user@@domain.com"))

    def test_invalid_start_special(self):
        """Starts with . or @"""
        self.assertFalse(is_valid_email(".user@domain.com"))
        self.assertFalse(is_valid_email("@user@domain.com"))

    def test_invalid_end_special(self):
        """Ends with . or @"""
        self.assertFalse(is_valid_email("user@domain.com."))
        self.assertFalse(is_valid_email("user@domain@"))

    def test_invalid_empty(self):
        """Empty or whitespace"""
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("   "))

    def test_invalid_spaces(self):
        """Spaces in email"""
        self.assertFalse(is_valid_email("user name@domain.com"))


# =============================================
# STEP 2: IMPLEMENT FUNCTION TO PASS ALL TESTS
# =============================================
def is_valid_email(email):
    """
    Validate email with strict rules.
    Returns True if valid, False otherwise.
    """
    if not email or email.isspace():
        return False

    # Rule 1: Only one @
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    # Rule 2: Local part rules
    if not local or local[0] in '.@' or local[-1] in '.@':
        return False
    if ' ' in local:
        return False

    # Rule 3: Domain part rules
    if not domain or domain[0] in '.@' or domain[-1] in '.@':
        return False
    if ' ' in domain or '..' in domain:
        return False

    # Rule 4: Must have at least one dot in domain
    if '.' not in domain:
        return False

    return True


# =============================================
# RUN TESTS
# =============================================
if __name__ == '__main__':
    unittest.main(verbosity=2)