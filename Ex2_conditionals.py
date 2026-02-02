# -------------------------------------------
# Exercise 2: Conditional Statements
# -------------------------------------------
#
# GOAL:
# 1. Master decision making in Python (if, elif, else).
# 2. Practise the Pair Programming Workflow: Driver vs Navigator.
# 3. Learn to sync code between team members (Push & Pull).
#
# CONCEPT:
# Conditionals allow your code to make choices, like a fork in the road.
# - if: "If it is raining, take an umbrella."
# - elif: "Otherwise, if it is sunny, take sunglasses."
# - else: "Otherwise (for anything else), just go outside."
#
# PAIR PROGRAMMING RULES:
# - The DRIVER types the code.
# - The NAVIGATOR reads the instructions and guides the driver.
# - You will SWITCH roles and computers after every task!
# -------------------------------------------


# -------------------------------------------
# Task 1: Simple Decisions (if)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Simple Decisions\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable called 'number' and assign it any integer you like.
# 2. Write an 'if' statement:
#    - Check IF the number is greater than 0.
#    - If it is, print "The number is positive."
# 3. Write a second (separate) 'if' statement:
#    - Check IF the number is even (Hint: number % 2 == 0).
#    - If it is, print "The number is even."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Task 1 complete"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: Two-Way Logic (if - else)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer. Get the latest code!
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: Two-Way Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Update your first check from Task 1:
#    - Add an 'else' block.
#    - If the number is NOT positive, print "The number is zero or negative."
# 2. Update your second check from Task 1:
#    - Add an 'else' block.
#    - If the number is NOT even, print "The number is odd."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Task 2 complete"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: Multi-Way Logic (if - elif - else)
# -------------------------------------------
# INSTRUCTION: Get the code from the previous Driver.
# 1. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: Multi-Way Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Comment out your code from Tasks 1 and 2 (so it doesn't run).
# 2. Create a variable called 'temperature'.
# 3. Write a chain of logic:
#    - IF temp is greater than 30, print "It's hot!"
#    - ELIF temp is greater than 15, print "It's mild."
#    - ELIF temp is greater than 0, print "It's cold."
#    - ELSE print "It's freezing!"
# 4. Test it by changing the variable value.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Task 3 complete"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Exam Grade Calculator
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "Extension 1: Exam Grade Calculator\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their exam score (0 to 100).
#    (Remember to convert the input to an integer).
# 2. Use if/elif/else to print the grade:
#    - Greater than or equal to 90: "Grade A"
#    - Greater than or equal to 80: "Grade B"
#    - Greater than or equal to 70: "Grade C"
#    - Otherwise: "Please retake the exam."

# Write your code below:


# Extension 2: The Login System
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: The Login System\n"
    + "-------------------------------------------")

# TODO:
# 1. Set a variable 'correct_password' to "secret123".
# 2. Ask the user to input a password.
# 3. Check the input:
#    - IF it matches exactly: print "Access Granted".
#    - ELIF it matches "Secret123" (wrong case): print "Close! Check your caps lock."
#    - ELSE: print "Access Denied".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Completed extensions"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The FizzBuzz Challenge
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The FizzBuzz Challenge\n"
    + "-------------------------------------------")

# This is the most famous programming interview question in the world!
#
# TODO:
# 1. Ask the user for a number.
# 2. Check the number against these rules (Order matters!):
#    - If divisible by 3 AND 5: Print "FizzBuzz"
#    - If divisible by only 3: Print "Fizz"
#    - If divisible by only 5: Print "Buzz"
#    - Otherwise: Print the number itself.
#
# HINT:
# Check the "FizzBuzz" condition FIRST. Why?
# If a number is 15, it is divisible by 3. If you check that first,
# the code will stop and print "Fizz" instead of "FizzBuzz".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Completed FizzBuzz challenge"
#    git push origin main
# -------------------------------------------
