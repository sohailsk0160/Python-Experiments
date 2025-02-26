import tkinter as tk
from tkinter import messagebox

def submit_form():
    """Handles form submission."""
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    email = entry_email.get()
    course = course_var.get()

    if not name or not age or not gender or not email or not course:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        age = int(age)  # Convert age to integer
    except ValueError:
        messagebox.showerror("Error", "Age must be a number!")
        return

    # Display student details
    messagebox.showinfo("Registration Successful",
                        f"Name: {name}\nAge: {age}\nGender: {gender}\nEmail: {email}\nCourse: {course}")

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")

# Heading
tk.Label(root, text="Student Registration Form", font=("Arial", 14, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Age (✅ FIXED)
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)  # ✅ Fixed issue here
entry_age.pack()

# Gender
tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="Select")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Email
tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Course Selection
tk.Label(root, text="Select Course:").pack()
course_var = tk.StringVar(value="Select")
courses = ["Python", "Java", "Web Development", "Data Science"]
tk.OptionMenu(root, course_var, *courses).pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()
