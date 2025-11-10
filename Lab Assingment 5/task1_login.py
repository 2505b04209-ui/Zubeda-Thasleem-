"""
TASK 1: Privacy and Data Security – Login System
Generated: Manually (Copilot not working)
Purpose: Show secure vs insecure login practices
"""

# =============================================
# 1. INSECURE VERSION (AI might generate this)
# =============================================
def insecure_login(username, password):
    """
    WARNING: NEVER DO THIS!
    - Hardcoded credentials
    - Plain text password
    - No input validation
    """
    # Hardcoded username & password (BIG SECURITY RISK!)
    HARDCODED_USER = "admin"
    HARDCODED_PASS = "12345"

    # Direct comparison – no hashing
    if username == HARDCODED_USER and password == HARDCODED_PASS:
        return True
    else:
        return False


# =============================================
# 2. SECURE VERSION (CORRECT WAY)
# =============================================
import hashlib  # For password hashing
import getpass  # For hidden input

def secure_login(username, password):
    """
    Secure login with:
    - Hashed password storage
    - Input validation
    - No hardcoded secrets
    - Hidden password input
    """
    # --- Step 1: Input Validation ---
    if not username or not password:
        print("Error: Username and password cannot be empty!")
        return False

    if len(username) < 3 or len(password) < 6:
        print("Error: Username >= 3 chars, Password >= 6 chars")
        return False

    # --- Step 2: Hash the input password ---
    # Using SHA-256 (secure one-way hash)
    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    # --- Step 3: Compare with stored hash (simulate DB) ---
    # In real app: fetch from secure database
    STORED_HASH = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"  # hash of "MyPass123"

    if hashed_input == STORED_HASH:
        print(f"Welcome, {username}! Login successful.")
        return True
    else:
        print("Invalid credentials. Try again.")
        return False


# =============================================
# 3. MAIN PROGRAM WITH EXAMPLES
# =============================================
def main():
    print("="*50)
    print("TASK 1: LOGIN SYSTEM – SECURITY ANALYSIS")
    print("="*50)

    # --- Example 1: Insecure Login (DEMO ONLY) ---
    print("\n1. INSECURE LOGIN (DO NOT USE IN REAL APP)")
    print("-" * 40)
    result1 = insecure_login("admin", "12345")
    print(f"Login result: {result1}")  # True

    # --- Example 2: Secure Login (REAL-WORLD READY) ---
    print("\n2. SECURE LOGIN (RECOMMENDED)")
    print("-" * 40)
    print("Try login with: username='alice', password='MyPass123'")
    # Simulate user input
    result2 = secure_login("alice", "MyPass123")
    print(f"Login result: {result2}")  # True

    # --- Example 3: Failed Login ---
    print("\n3. FAILED LOGIN TEST")
    result3 = secure_login("bob", "wrongpass")
    print(f"Login result: {result3}")  # False

    # --- Example 4: Empty Input ---
    print("\n4. INPUT VALIDATION TEST")
    result4 = secure_login("", "short")
    print(f"Login result: {result4}")  # False + Error message


# =============================================
# RUN THE PROGRAM
# =============================================
if __name__ == "__main__":
    main()