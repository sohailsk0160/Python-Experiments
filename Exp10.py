def append_to_file(filename, text):
    """Appends text to the given file."""
    try:
        with open(filename, "a") as file:  # Open file in append mode
            file.write(text + "\n")  # Append new text with a newline
        print("Text appended successfully!")
    except IOError:
        print("Error: Unable to write to file.")

def display_file_content(filename):
    """Reads and displays the entire file content."""
    try:
        with open(filename, "r") as file:  # Open file in read mode
            content = file.read()
            print("\nFile Content:\n" + content)
    except FileNotFoundError:
        print("Error: File not found!")
    except IOError:
        print("Error: Unable to read file.")

# Get user input
filename = input("Enter filename: ")
text = input("Enter text to append: ")

# Append text to file
append_to_file(filename, text)

# Display file content
display_file_content(filename)
