# -*- coding: utf-8 -*-
"""password_checker

A beginner Python project that checks password strength.
"""

password = input("Enter a password: ")
score = 0
common = ["123456", "password", "12345678", "abc123", "helloworld", "111111"]

if len(password) >= 8:
    print("Long enough")
    score += 1
else:
    print("Too short")

if any(c.islower() for c in password):
    print("Has a lowercase letter")
    score += 1
else:
    print("Add a lowercase letter")

if any(c.isupper() for c in password):
    print("Has an uppercase letter")
    score += 1
else:
    print("Add an uppercase letter")

if any(c.isdigit() for c in password):
    print("Has a number")
    score += 1
else:
    print("Add a number")

if any(not c.isalnum() for c in password):
    print("Has a symbol")
    score += 1
else:
    print("Add a symbol like ! or @")

if password.lower() not in common:
    print("Not a common password")
    score += 1
else:
    print("This is a very common password")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")
