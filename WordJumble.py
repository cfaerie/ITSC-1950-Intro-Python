#Program Name: Word Jumble
#Date: 1/31/13
#Developer: ITCS 1950 Friday Class - Rachel Sanford

#This program will be the improved version of the word jumble game
#already present in the textbook. This version will pair each word with a hint.
#When the player enters "Hint", the program will display it.

#The computer picks a random word and then "jumbles" it
#The player has to guess the original word

import random

#create a sequence of words to choose from
WORDS = ("python","jumble","easy","difficult","answer","xylophone")

#pick one word randomly from sequence
word = random.choice(WORDS)

#create variable to use later to see if guess is correct
correct = word

#create jumbled version of the word
jumble = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#start the game
print
"""
           Welcome to Word Jumble!
           
    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
"""
print "The jumble is:", jumble

guess = raw_input("\nYour guess: ")
guess = guess.lower()
while (guess != correct) and (guess!= ""):
    if guess !=correct and guess != "hint":
        print "Sorry, that's not it."
        
    guess = raw_input("Your guess: ")
    guess = guess.lower()
    if guess == "hint":
        HINTS = ("a basic programming software",
                 "The name of the game",
                 "_____ peasy lemon squeeze",
                 "hard", "Opposite of question",
                 "a musical instrument")
        if correct == "python":
            print HINTS[0]
        elif correct == "jumble":
            print HINTS[1]
        elif correct == "easy":
            print HINTS[2]
        elif correct == "difficult":
            print HINTS[3]
        elif correct == "answer":
            print HINTS[4]
        elif correct == "xylophone":
            print HINTS[5]
            

if guess == correct:
    print "That's it! You guessed it!\n"

print "Thanks for playing."
raw_input("\n\nPress the enter key to exit.")
