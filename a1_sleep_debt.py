"""
CP1401 2021-1 Assignment 1
Program 1 – Sleep Debt Calculator
Student Name: Rajkumar Senthilraj Ragulraj
Date started: 29/07/2021

Pseudocode:

print(Sleep debt calculator)
NO_OF_NIGHTS = 5
RECOMMENDED = 40
total = 0
create a for loop: range(1, NO_OF_NIGHTS + 1)
create temporary variable under the for loop: new_input
create while statement error checking
if total sleep >=  RECOMMENDED
print(You are getting enough sleep. Keep it up!)
if total sleep < RECOMMENDED
print(Your sleep debt over this time:", RECOMMENDED - total)
"""

print("Sleep debt calculator")
NO_OF_NIGHTS = 5
RECOMMENDED = 40
total = 0
for hours in range(1, NO_OF_NIGHTS + 1):
    new_input = float(input(f"Night {hours} hours sleep: "))
    while new_input < 0 or new_input > 24:
        print("Invalid number of hours.")
        new_input = float(input(f"Night {hours} hours sleep: "))
    total += new_input
print("recommended total sleep is:", RECOMMENDED)
print("Your total hours of sleep:", total)
if total >= RECOMMENDED:
    print("You are getting enough sleep. Keep it up!")
else:
    print("Your sleep debt over this time:", RECOMMENDED - total)