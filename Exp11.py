import re

def extract_data_from_file(filename, pattern):
    """Reads a file and extracts data matching a given regex pattern."""
    try:
        with open(filename, "r") as file:
            content = file.read()  # Read entire file content
            
        matches = re.findall(pattern, content)  # Find all occurrences of the pattern
        
        if matches:
            print("\nExtracted Data:")
            for match in matches:
                print(match)
        else:
            print("\nNo matching data found!")
    
    except FileNotFoundError:
        print("Error: File not found!")
    except IOError:
        print("Error: Unable to read file!")

# Get user input for filename and regex pattern
filename = input("Enter the filename: ")
pattern = input("Enter the regular expression pattern: ")

# Call function to extract data
extract_data_from_file(filename, pattern)
