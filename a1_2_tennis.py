"""
CP1401 2021-1 Assignment 1
Program 2 – Tennis Results
Student Name: Rajkumar Senthilraj Ragulraj
Date started: 29/07/2021

Pseudocode:

print(Welcome player 1. how was your match?)

get your score
get opponents score
MORE THAN 8 = opponent score + your score >= 8

if your score > opponents score
print(You won! :))
if your score > opponents score and MORE THAN 8 == True
print(Congratulations on playing a fast game!)
if your score < opponents score
print(You lost :( Keep trying!)
if your score < opponents score and MORE THAN 8 == True
print(Congratulations on playing a fast game!)
if your score == opponents score
print(It's a draw!)
if your score == opponents score and MORE THAN 8 == True
print(Congratulations on playing a fast game!)
"""

print("Welcome Player 1. How was your match?")

your_score = int(input("Your Score: "))
opponent_score = int(input("Opponent Score: "))
EIGHT_OR_MORE_GAMES = opponent_score + your_score >= 8

if your_score > opponent_score:
    print("You won! :)")
    if your_score > opponent_score and EIGHT_OR_MORE_GAMES:
        print("Congratulations on playing a fast game!")

if your_score < opponent_score:
    print("You lost :( Keep trying!")
    if your_score < opponent_score and EIGHT_OR_MORE_GAMES:
        print("Congratulations on playing a fast game!")

if your_score == opponent_score:
    print("It's a draw!")
    if your_score == opponent_score and EIGHT_OR_MORE_GAMES:
        print("Congratulations on playing a fast game!")
