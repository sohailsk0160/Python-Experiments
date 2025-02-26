def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b  # ZeroDivisionError if b is 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid integers!")

def access_list_element():
    try:
        my_list = [10, 20, 30, 40, 50]
        index = int(input(f"Enter index (0 to {len(my_list)-1}): "))
        print(f"Element at index {index}: {my_list[index]}")  # IndexError if out of range
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Please enter a valid integer index!")

def open_file():
    try:
        filename = input("Enter filename to open: ")
        with open(filename, "r") as file:
            content = file.read()
            print("File content:\n", content)  # FileNotFoundError if file does not exist
    except FileNotFoundError:
        print("Error: File not found!")
    except IOError:
        print("Error: Issue reading the file!")

def convert_string_to_int():
    try:
        num_str = input("Enter a number as a string: ")
        num = int(num_str)  # ValueError if input is not a number
        print(f"Converted number: {num}")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")

def key_error_handling():
    try:
        my_dict = {"name": "Alice", "age": 25}
        key = input("Enter key to access value: ")
        print(f"Value: {my_dict[key]}")  # KeyError if key does not exist
    except KeyError:
        print("Error: Key not found in dictionary!")

while True:
    print("\nMENU-DRIVEN EXCEPTION HANDLING PROGRAM")
    print("1. Divide Numbers (ZeroDivisionError, ValueError)")
    print("2. Access List Element (IndexError, ValueError)")
    print("3. Open a File (FileNotFoundError, IOError)")
    print("4. Convert String to Integer (ValueError)")
    print("5. Access Dictionary Key (KeyError)")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            divide_numbers()
        elif choice == 2:
            access_list_element()
        elif choice == 3:
            open_file()
        elif choice == 4:
            convert_string_to_int()
        elif choice == 5:
            key_error_handling()
        elif choice == 6:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Error: Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Error: Please enter a valid menu option (integer).")
