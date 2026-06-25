# user_input.py

from datetime import datetime

# Get current year
current_year = datetime.now().year

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Enter your favorite programming language: ")

# Calculate the year when the user turns 100
year_turn_100 = current_year + (100 - age)

# Display results
print("\n----- User Profile -----")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite programming language is {language}.")
print(f"You will turn 100 years old in the year {year_turn_100}.")