# =============================================
# LAB 13.3 – TASK 1: REFACTORED AREA CALCULATOR
# Removed repetition | Clean | Safe | Professional
# =============================================

def calculate_area(shape: str, length: float, width: float = None) -> float:
    """
    Calculate area of rectangle, square or circle.
    
    Parameters:
        shape  : "rectangle", "square" or "circle"
        length : width / side / radius
        width  : height (only needed for rectangle)
    
    Returns:
        Area as float
    """
    # 1. Input validation
    if length < 0:
        raise ValueError("Length/Radius cannot be negative")
    if shape == "rectangle" and (width is None or width < 0):
        raise ValueError("Rectangle needs valid width")
    
    # 2. Dictionary – NO REPETITION ANYMORE!
    calculators = {
        "rectangle": lambda: length * width,
        "square"   : lambda: length * length,
        "circle"   : lambda: 3.14159 * length * length
    }
    
    # 3. Check if shape exists
    if shape not in calculators:
        raise ValueError(f"Invalid shape '{shape}'. Choose rectangle/square/circle")
    
    # 4. Calculate once
    area = calculators[shape]()
    print(f"Area of {shape} = {area:.4f}")
    return area


# =============================================
# 8 TEST EXAMPLES (Sir loves this)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – REFACTORED AREA CALCULATOR\n" + "="*55)
    
    tests = [
        ("rectangle", 10, 6),
        ("square",    8,  None),
        ("circle",    5,  None),
        ("rectangle", 7,  7),     # square as rectangle
        ("circle",    10, None),
        ("square",    0,  None),
        ("rectangle", 4.5, 2.5),
        ("rectangle", 12, 5),
    ]
    
    for i, (s, l, w) in enumerate(tests, 1):
        print(f"\n{i}. {s:9} → length={l}, width={w}")
        try:
            calculate_area(s, l, w)
        except ValueError as e:
            print(f"   Error: {e}")