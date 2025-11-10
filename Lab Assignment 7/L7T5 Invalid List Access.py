# =============================================
# TASK 5: INDEX ERROR – Invalid List Access
# =============================================
# Prompt: "Fix index error: lst = [1,2,3] print(lst[5])"

lst = [1, 2, 3]
index = 5

if index < len(lst):  # Added bounds check
    print("Task 5:", lst[index])
else:
    print("Task 5: Index out of range! Safe access used.")
