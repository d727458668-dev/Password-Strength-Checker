import tkinter as tk
from tkinter import messagebox
""" if not work this code .
    you want dounload pip packages.
    pip install tkinter and pip install messagebox.
    I already run and check the tool properly. """
def check_password():
    password = entry.get()
    missing = []

    if len(password) < 8:
        missing.append("• Minimum 8 characters")

    if not any(c.isupper() for c in password):
        missing.append("• At least one uppercase letter")

    if not any(c.islower() for c in password):
        missing.append("• At least one lowercase letter")

    if not any(c.isdigit() for c in password):
        missing.append("• At least one number")

    if not any(not c.isalnum() for c in password):
        missing.append("• At least one special character")

    if not password:
        messagebox.showwarning("Warning", "Password cannot be empty")
        return

    if not missing:
        strength = "STRONG"
        color = "green"
        feedback = "Password meets all security criteria!"
    elif len(missing) <= 2:
        strength = "MEDIUM"
        color = "orange"
        feedback = "\n".join(missing)
    else:
        strength = "WEAK"
        color = "red"
        feedback = "\n".join(missing)

    result_label.config(text=f"Password Strength: {strength}", fg=color)
    feedback_label.config(text=feedback)


# GUI Window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="Password Complexity Checker",
         font=("Arial", 16, "bold")).pack(pady=10)

# Password Entry
tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Check Button
tk.Button(root, text="Check Strength",
          command=check_password,
          width=15).pack(pady=10)

# Result Labels
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

feedback_label = tk.Label(root, text="", justify="left")
feedback_label.pack(pady=5)

root.mainloop()