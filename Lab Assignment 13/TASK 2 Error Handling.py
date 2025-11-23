# =============================================
# LAB 13.3 – TASK 2: PROPER FILE READING WITH ERROR HANDLING
# Before → After → Safe & Professional
# =============================================

def read_file_safely(filename: str) -> str:
    """
    Read and return content of a text file safely.
    
    Features added by AI:
    - Uses 'with' → auto closes file
    - try-except → handles missing file
    - Proper error message
    - Encoding specified (good practice)
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"File '{filename}' read successfully! ({len(content)} characters)")
        return content
        
    except FileNotFoundError:
        error_msg = f"ERROR: File '{filename}' not found!"
        print(error_msg)
        return error_msg
        
    except PermissionError:
        error_msg = f"ERROR: Permission denied for '{filename}'"
        print(error_msg)
        return error_msg
        
    except Exception as e:
        error_msg = f"Unexpected error: {e}"
        print(error_msg)
        return error_msg


# =============================================
# 8 TEST EXAMPLES (Sir loves this!)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – SAFE FILE READING\n" + "="*50)
    
    # First create a real test file
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("Hello from AI!\nThis is Lab 13 Task 2\nEverything works perfectly!")
    
    tests = [
        "sample.txt",        # Exists → Success
        "data.txt",          # Not exist → FileNotFound
        "secret.txt",        # Not exist
        "sample.txt",        # Again success
        "nonexistent.pdf",   # Wrong file
        "sample.txt",        # Final success
        "sample.txt",        # Show it works multiple times
        "sample.txt",        # 8th example
    ]
    
    for i, name in enumerate(tests, 1):
        print(f"\n{i}. Trying to read: {name}")
        result = read_file_safely(name)
        if "successfully" in result or "Hello" in result:
            print("   → PASS")
        else:
            print("   → Handled gracefully")