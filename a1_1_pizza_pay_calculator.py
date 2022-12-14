"""
CP1401 2021-1 Assignment 1
Program 1 – Pizza Pay Calculator
Student Name: Rajkumar Senthilraj Ragulraj
Date started: 29/07/2021

Pseudocode:

Create 2 variables
WARM PIZZA = 1.45
TRIP = 0.95
find number of trips
find number of minutes
trip cost = WARM PIZZA * number of trips
minutes cost = TRIP * number of minutes
total = trip cost + minutes cost
print(pay for number f trips)
print(pau for number of minutes)
print(total pay)
"""

WARM_PIZZA = 1.45
PER_TRIP = 0.95

print("Warm Pizza Pay Calculator")
number_of_trips = float(input("Number of trips: "))
number_of_minutes = float(input("Number of minutes:  "))

trip_cost = WARM_PIZZA * number_of_trips
min_cost = PER_TRIP * number_of_minutes
total = trip_cost + min_cost

print("For", number_of_trips, "trips your pay is: $", trip_cost)
print("For", number_of_minutes, "minutes your pay is: $", min_cost)
print("Your total pay is:$ ", trip_cost + min_cost)





