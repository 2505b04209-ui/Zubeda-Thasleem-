# =============================================
# LAB 12.3 – TASK 4: GRADIENT DESCENT (NO MATPLOTLIB)
# Function: f(x) = 2x³ + 4x + 5 → BUT HAS NO MINIMUM!
# We will prove it + show correct parabola version
# =============================================

def f_cubic(x):
    """Given function: f(x) = 2x³ + 4x + 5"""
    return 2 * x**3 + 4 * x + 5

def df_cubic(x):
    """Derivative: f'(x) = 6x² + 4 → Always positive!"""
    return 6 * x**2 + 4

def f_parabola(x):
    """Correct function that HAS minimum: f(x) = 2x² + 4x + 5"""
    return 2 * x**2 + 4 * x + 5

def df_parabola(x):
    """Derivative: f'(x) = 4x + 4 → Zero at x = -1"""
    return 4 * x + 4

def gradient_descent(func, deriv, start_x, lr=0.01, max_steps=100,
                         tolerance=0.0001):
    """Simple Gradient Descent – No external library"""
    x = start_x
    print(f"Starting at x = {x:.4f} → f(x) = {func(x):.4f}")
    print("Step   |     x      |   f(x)    |  slope")
    print("-" * 45)
    
    for step in range(max_steps):
        slope = deriv(x)
        new_x = x - lr * slope
        
        print(f"{step:3d}    | {x:8.4f}  | {func(x):8.4f}  | {slope:6.3f}")
        
        if abs(slope) < tolerance:
            print(f"\nCONVERGED! Minimum at x ≈ {x:.6f}")
            print(f"Minimum value f(x) ≈ {func(x):.6f}")
            return x, func(x)
        
        x = new_x
    
    print(f"\nStopped after {max_steps} steps")
    return x, func(x)


# =============================================
# MAIN – 8 EXAMPLES + EXPLANATION
# =============================================
if __name__ == "__main__":
    print("LAB 12.3 – TASK 4: GRADIENT DESCENT ANALYSIS")
    print("="*70)
    
    print("1. Given function: f(x) = 2x³ + 4x + 5")
    print("   Derivative: f'(x) = 6x² + 4")
    print("   → 6x² + 4 is ALWAYS ≥ 4 > 0 → NO MINIMUM EXISTS!")
    print("   Function goes to +∞ as x → ±∞\n")
    
    print("Trying gradient descent anyway (will go to -∞):")
    gradient_descent(f_cubic, df_cubic, start_x=2.0, lr=0.01, max_steps=20)
    
    print("\n" + "="*70)
    print("2. CORRECTED FUNCTION (Most likely intended):")
    print("   f(x) = 2x² + 4x + 5  → Parabola with minimum")
    print("   Derivative: 4x + 4 = 0 → x = -1")
    print("   Minimum value: f(-1) = 3\n")
    
    print("Running Gradient Descent on correct parabola:")
    min_x, min_val = gradient_descent(f_parabola, df_parabola, start_x=5.0, lr=0.1)
    
    print("\n" + "="*70)
    print("8 DIFFERENT STARTING POINTS (All converge to x = -1):")
    starts = [10, -5, 0, 3, -2, 1.5, -10, 0.5]
    for i, start in enumerate(starts, 1):
        print(f"\n{i}. Start x = {start}")
        x, val = gradient_descent(f_parabola, df_parabola, start, lr=0.1, max_steps=50)
        print(f"   → Converged to x ≈ {x:.6f}, f(x) ≈ {val:.6f}")