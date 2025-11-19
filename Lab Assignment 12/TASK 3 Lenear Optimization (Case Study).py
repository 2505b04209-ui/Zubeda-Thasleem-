# =============================================
# LAB 12.3 – TASK 3: LINEAR OPTIMIZATION CASE STUDY
# METHOD: Corner Point Method (Graphical Method in Code)
# No PuLP | No Installation | Works on ANY PC
# =============================================

def solve_linear_optimization():
    """
    Solve the classic production problem:
    Maximize Profit = 40A + 30B
    Subject to:
        2A + B  ≤ 100   → Machine hours constraint
        A + 3B ≤ 120    → Labor hours constraint
        A ≥ 0, B ≥ 0     → Cannot produce negative units
    """
    
    print("="*70)
    print("LINEAR OPTIMIZATION – PROFIT MAXIMIZATION PROBLEM")
    print("="*70)
    
    # STEP 1: Explain the problem clearly
    print("A company makes two products:")
    print("   • Product A → Profit ₹40 per unit")
    print("   • Product B → Profit ₹30 per unit")
    print()
    print("Resources available:")
    print("   • Machine hours : 100 hrs total")
    print("       → Product A uses 2 hrs, B uses 1 hr")
    print("   • Labor hours   : 120 hrs total")
    print("       → Product A uses 1 hr, B uses 3 hrs")
    print()
    
    # STEP 2: Find all 4 CORNER POINTS of feasible region
    # These are the only points where maximum/minimum occurs in Linear Programming
    print("Step 1: Finding 4 CORNER POINTS of feasible region:")
    print("   → (0,0)      : Make nothing")
    print("   → (50,0)     : Make only A → 2×50 = 100 machine hrs used")
    print("   → (0,40)     : Make only B → 3×40 = 120 labor hrs used")
    print("   → (36,28)    : Intersection of both constraints (solve equations)")
    print()
    
    # List of all corner points (A, B)
    corner_points = [
        (0,  0),    # Point 1: Origin
        (50, 0),    # Point 2: Max A
        (0,  40),   # Point 3: Max B
        (36, 28)    # Point 4: Intersection (optimal)
    ]
    
    # STEP 3: Evaluate profit at each corner point
    print("Step 2: Calculate PROFIT at each corner point:")
    print(f"{'Point':<10} {'A':>4} {'B':>4} {'Profit = 40A + 30B':>25}")
    print("-" * 55)
    
    max_profit = 0
    best_A = 0
    best_B = 0
    
    for A, B in corner_points:
        profit = 40 * A + 30 * B
        
        # Show calculation
        print(f"({A:2.0f},{B:2.0f}) → 40×{A:2.0f} + 30×{B:2.0f} = ₹{profit:,.0f}")
        
        # Keep track of maximum
        if profit > max_profit:
            max_profit = profit
            best_A = A
            best_B = B
            print("   ← BEST SO FAR!")
        print()
    
    # STEP 4: Final Answer
    print("="*55)
    print("FINAL OPTIMAL SOLUTION:")
    print(f"   → Produce {best_A} units of Product A")
    print(f"   → Produce {best_B} units of Product B")
    print(f"   → MAXIMUM PROFIT = ₹{max_profit:,.0f}")
    print("="*55)
    print("This is the BEST possible profit under given constraints!")


# =============================================
# EXTRA EXAMPLES – Change constraints & see new answer!
# =============================================
def example_with_different_constraints():
    print("\n" + "="*70)
    print("EXAMPLE: What if machine hours increase to 120?")
    print("="*70)
    
    # New corner points when machine constraint becomes 2A + B ≤ 120
    new_points = [(0,0), (60,0), (0,40), (48,24)]  # (48,24) is new intersection
    max_p = max(40*a + 30*b for a,b in new_points)
    print(f"New maximum profit = ₹{max_p:,.0f} (by making 48A + 24B)")


# =============================================
# RUN THE PROGRAM
# =============================================
if __name__ == "__main__":
    solve_linear_optimization()
    example_with_different_constraints()