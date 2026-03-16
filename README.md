#  Password Complexity Checker

A **Password Complexity Checker** is a simple desktop application built using **Python** and **Tkinter**.  
This tool allows users to test the strength of a password by verifying it against commonly recommended security rules.  
The application analyzes the password and provides feedback indicating whether the password is **Weak**, **Medium**, or **Strong**.

Passwords are an essential part of digital security. Weak passwords can easily be guessed or cracked by attackers.  
This project helps users understand how secure their passwords are and encourages the use of stronger passwords.

---

#  Project Overview

The **Password Complexity Checker** provides an interactive graphical interface where users can enter a password and instantly check its strength.  
The program evaluates the password using several validation rules and displays detailed feedback on missing requirements.

The goal of this project is to demonstrate:
- Basic **GUI development in Python**
- Use of **Tkinter widgets**
- **Password validation logic**
- **User interaction handling**
- Simple **security awareness tools**

---

# Features

- User-friendly **Graphical User Interface (GUI)**
- Real-time **password strength evaluation**
- Checks password against **multiple security conditions**
- Displays **Weak, Medium, or Strong** result
- Shows **specific feedback** for missing requirements
- Uses **color-coded strength indicators**
- Displays **warning message** if password field is empty
- Lightweight and easy to run

---

# 🔍 Password Validation Rules

The application checks the password for the following security conditions:

1. Password must contain **at least 8 characters**
2. Password must include **at least one uppercase letter**
3. Password must include **at least one lowercase letter**
4. Password must include **at least one numeric digit**
5. Password must include **at least one special character**

If all conditions are satisfied, the password is considered **Strong**.

---

# Password Strength Classification

| Strength Level | Description |
|----------------|-------------|
| 🔴 Weak | Password is missing multiple security requirements |
| 🟠 Medium | Password meets some requirements but not all |
| 🟢 Strong | Password meets all recommended security conditions |

---

# Graphical Interface Components

The application GUI includes the following components:

- **Window Title** – Displays the name of the application
- **Heading Label** – Shows the program title
- **Password Input Field** – Allows the user to type a password
- **Check Strength Button** – Triggers password validation
- **Result Label** – Displays password strength
- **Feedback Label** – Shows missing password requirements

---


---

#  Requirements

To run this project, you need:

- **Python 3.x**
- **Tkinter library**

Tkinter usually comes pre-installed with Python.  
If it is not installed on your system, you can install it using:

```bash
 pip install tkinter
