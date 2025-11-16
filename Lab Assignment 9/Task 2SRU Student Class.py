# =============================================
# LAB 9.3 – TASK 2: SRU Student Class
# Objective: Manual vs AI Inline Comments

# AI Tool
# =============================================

class SRUStudent:
    """
    A class to represent an SRU student with name, roll number, hostel 
    status, and fees.

    Attributes:
        name (str): Student's full name
        roll_no (str): Unique roll number
        hostel_status (bool): True if stays in hostel
        fees_paid (float): Total fees paid
    """
    
    # -------------------------------------------------
    # MANUAL: Constructor - Initialize student object
    # -------------------------------------------------
    def __init__(self, name, roll_no, hostel_status=False):
        # Store student's name
        self.name = name
        
        # Store unique roll number
        self.roll_no = roll_no
        
        # Set hostel status (default: False)
        self.hostel_status = hostel_status
        
        # Initialize fees paid to zero
        self.fees_paid = 0.0

    # -------------------------------------------------
    # MANUAL: Update fees by adding amount
    # -------------------------------------------------
    def fee_update(self, amount):
        # Validate that amount is positive
        if amount > 0:
            # Add amount to total fees
            self.fees_paid += amount
            # Print confirmation
            print(f"Fees updated: ₹{amount:.2f}")
        else:
            # Show error for invalid amount
            print("Error: Amount must be positive!")

    # -------------------------------------------------
    # MANUAL: Display all student details
    # -------------------------------------------------
    def display_details(self):
        # Print student's name
        print(f"Name: {self.name}")
        
        # Print roll number
        print(f"Roll No: {self.roll_no}")
        
        # Print hostel status
        print(f"Hostel: {'Yes' if self.hostel_status else 'No'}")
        
        # Print fees paid
        print(f"Fees Paid: ₹{self.fees_paid:.2f}")


# =============================================
# AI-GENERATED INLINE COMMENTS (By GROK)
# =============================================
# __init__: Sets name, roll_no, hostel_status; initializes fees_paid to 0
# fee_update: Adds positive amount to fees_paid; prints message
# display_details: Prints formatted student information in readable format


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – SRU STUDENT CLASS\n" + "="*50)

    # Example 1: Day scholar, no fees
    s1 = SRUStudent("Amit Sharma", "CSE001")
    print("1. Day Scholar (No Fees):")
    s1.display_details()
    print()

    # Example 2: Hostel student, pay fees
    s2 = SRUStudent("Priya Verma", "ECE002", True)
    s2.fee_update(25000)
    print("2. Hostel Student + Fees:")
    s2.display_details()
    print()

    # Example 3: Multiple fee updates
    s3 = SRUStudent("Rohan Kumar", "MECH003")
    s3.fee_update(15000)
    s3.fee_update(10000)
    print("3. Multiple Fee Updates:")
    s3.display_details()
    print()

    # Example 4: Invalid fee amount
    s4 = SRUStudent("Sneha Patel", "CIVIL004")
    s4.fee_update(-5000)  # Should show error
    print("4. Invalid Fee Amount:")
    s4.display_details()
    print()

    # Example 5: Empty name
    s5 = SRUStudent("", "IT005", True)
    s5.fee_update(30000)
    print("5. Empty Name (Still Works):")
    s5.display_details()
    print()

    # Example 6: Long roll number
    s6 = SRUStudent("Vikram Singh", "EEE-2025-001")
    print("6. Long Roll Number:")
    s6.display_details()
    print()

    # Example 7: Zero fees
    s7 = SRUStudent("Neha Gupta", "BIO006")
    print("7. Zero Fees:")
    s7.display_details()
    print()

    # Example 8: Full profile
    s8 = SRUStudent("Arjun Reddy", "MBA007", True)
    s8.fee_update(50000)
    s8.fee_update(20000)
    print("8. Full Profile:")
    s8.display_details()