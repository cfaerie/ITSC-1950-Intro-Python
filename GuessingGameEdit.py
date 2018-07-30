#Program Name: Guess My Number Program
#Date: 1/25/13
#Developer: ITCS 1950 Friday Class - Rachel

#This program is a guess my number game where the player only has 5 chances
#to guess the number. When the 5 chances are over, the program will end
#and tell the user a chastising message
import random

def ask_number(question, low, high):
    """Ask for a number within range."""
    response = None
    while response not in range(low,high):
        response = int(raw_input(question))
    return response

print "Welcome to Guess My Number!"
print "I'm thinking of a number betwen 1 and 100."
print "Try to guess it in no more than 5 atttempts."
q = "Give me a number between 1 and 100: "

#Set initial values
the_number =  random.randrange(100) +1
guess = ask_number(q,1,100)
tries = 1

while (guess != the_number and tries <=4):
    if(guess > the_number):
        print "Lower..."
    elif(guess < the_number):
        print "Higher..."

    guess = ask_number(q,1,100)
    tries += 1
if guess == the_number:
    print"You got it! Good job!"
else:
    print "You lose slowpoke!"
