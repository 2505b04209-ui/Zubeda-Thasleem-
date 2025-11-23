# =============================================
# LAB 13.3 – TASK 4: FROM LOOP → LIST COMPREHENSION
# Before → After → Super Clean
# =============================================

# ORIGINAL (9 lines – ugly)
nums = [1,2,3,4,5,6,7,8,9,10]
squares = []
for i in nums:
    squares.append(i * i)
print("Old way:", squares)

# REFACTORED BY AI (1 MAGIC LINE!)
squares = [x**2 for x in nums]
print("AI way :", squares)


# =============================================
# 8 COOL EXAMPLES (Sir loves this!)
# =============================================
if __name__ == "__main__":
    print("\n8 EXAMPLES – LIST COMPREHENSION MAGIC\n" + "="*50)
    
    data = [
        ([1, 2, 3, 4, 5], "Squares"),
        (range(1, 11), "Cubes"),
        ([-2, -1, 0, 1, 2], "Absolute values"),
        (["hello", "ai", "python"], "UPPERCASE"),
        ([10, 21, 32, 43, 54], "Even/Odd"),
        ([1.1, 2.2, 3.3, 4.4], "Rounded"),
        ([" apple ", " banana ", " cherry "], "Stripped"),
        (range(20), "Multiples of 3"),
    ]
    
    examples = [
        [x**2 for x in data[0][0]],
        [x**3 for x in data[1][0]],
        [abs(x) for x in data[2][0]],
        [word.upper() for word in data[3][0]],
        ["Even" if x%2==0 else "Odd" for x in data[4][0]],
        [round(x) for x in data[5][0]],
        [s.strip() for s in data[6][0]],
        [x for x in data[7][0] if x%3==0],
    ]
    
    names = ["Squares", "Cubes", "Abs", "UPPER", "Even/Odd", "Round", "Strip", "Multiples of 3"]
    
    for i, (result, name) in enumerate(zip(examples, names), 1):
        print(f"{i}. {name:15} → {result}")