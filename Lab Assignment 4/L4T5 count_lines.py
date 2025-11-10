def count_lines_in_file(filename: str) -> int:
    """
    Count the total number of lines in a text file, including empty lines.
    
    Args:
        filename (str): Path to the text file to count lines in
    
    Returns:
        int: Total number of lines in the file (0 for empty files)
    
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
        TypeError: If filename is not a string
    
    Examples:
        # File: sample.txt containing 5 lines:
        # Line 1
        # Line 2
        # Line 3
        # Line 4
        # Line 5
        # count_lines_in_file("sample.txt") -> 5
        
        # File: notes.txt with blank lines:
        # First paragraph
        #
        # Second paragraph
        #
        # Third paragraph
        # count_lines_in_file("notes.txt") -> 5
        
        # Empty file:
        # count_lines_in_file("empty.txt") -> 0
    """
    # Input validation
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    
    try:
        # Open the file in read mode
        # Using 'with' ensures the file is properly closed after we're done
        with open(filename, 'r', encoding='utf-8') as file:
            # readlines() returns a list of all lines in the file
            # len() counts how many lines are in this list
            # Note: Each line in the list includes the trailing newline character
            return len(file.readlines())
            
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        raise FileNotFoundError(f"The file '{filename}' was not found")
    except IOError as e:
        # Handle other potential file reading errors
        raise IOError(f"Error reading file '{filename}': {str(e)}")

# Example usage and test cases
def run_tests():
    """Run example test cases with different sample files."""
    
    # First, let's create some sample files for testing
    
    # Sample 1: File with 5 lines
    with open('sample1.txt', 'w', encoding='utf-8') as f:
        f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")
    
    # Sample 2: Empty file
    with open('empty.txt', 'w', encoding='utf-8') as f:
        f.write("")
    
    # Sample 3: File with blank lines
    with open('notes.txt', 'w', encoding='utf-8') as f:
        f.write("First paragraph\n\nSecond paragraph\n\nThird paragraph\n")
    
    # Now let's test our function with these files
    print("=== Line Counter Test Cases ===")
    print("-" * 30)
    
    # Test 1: Regular file with 5 lines
    try:
        count = count_lines_in_file('sample1.txt')
        print(f"sample1.txt: {count} lines")
    except Exception as e:
        print(f"Error with sample1.txt: {str(e)}")
    
    # Test 2: Empty file
    try:
        count = count_lines_in_file('empty.txt')
        print(f"empty.txt: {count} lines")
    except Exception as e:
        print(f"Error with empty.txt: {str(e)}")
    
    # Test 3: File with blank lines
    try:
        count = count_lines_in_file('notes.txt')
        print(f"notes.txt: {count} lines")
    except Exception as e:
        print(f"Error with notes.txt: {str(e)}")
    
    # Test 4: Non-existent file (should show error handling)
    try:
        count = count_lines_in_file('nonexistent.txt')
        print(f"nonexistent.txt: {count} lines")
    except Exception as e:
        print(f"Error with nonexistent.txt: {str(e)}")

def main():
    """
    Main function to handle user interaction for counting lines in a file.
    Prompts user for a file path and displays the line count or error message.
    """
    print("=== File Line Counter ===")
    print("Enter the path to a text file to count its lines.")
    
    # Get file path from user
    file_path = input("File path: ").strip()
    
    try:
        # Count lines and display result
        line_count = count_lines_in_file(file_path)
        print(f"\nThe file '{file_path}' contains {line_count} lines.")
    
    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
        print("Please check the file path and try again.")
    
    except IOError as e:
        print(f"\nError reading the file: {str(e)}")
        print("Please make sure you have permission to access the file.")
    
    except TypeError:
        print("\nError: Invalid file path provided.")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Change this to True to run tests instead of user interaction
    RUN_TESTS = False
    
    if RUN_TESTS:
        run_tests()
    else:
        main()