# ITSC 1950 Intro Python

HW1 - AveGameScore.py
Program takes input of 2 "scores" from user.
It calculates the average, then outputs that average to the screen.

HW3 - GuessingGame.py
Program generates a random number between 1 and 100.
Program allows user to enter guesses up to 5 times. 
Program will tell the user whether they need to guess higher or lower than their last guess.
If user guesses the correct number in 5 tries or less, the program ends. It displays a winning message.
If user uses all 5 tries and still hasn't guessed the number, the program ends.
It displays a losing message

HW4 - WordJumble.py
Program creates a sequence of words to choose from. 
One word will be randomly selected to use.
Program will create a scrambled version of that word and print to screen.
There are set hints that correspond with certain words. The program will give these hints
if user wants them.
Program continues to loop until the user correctly enters the unscrambled word.

HW5 - GuessingGameEdit.py
NOTE: Very similar to HW3, with slight modifications. A function called "ask_number" was 
created to contain/handle gathering the user input.
Program is a "Guess my Number" game where the player has only 5 chances to guess the number.
If the number isn't guessed before the 5 chances are over, a losing message is displayed.
If the number is guessed before the 5 chances are up, a winning message displays.

HW6 - DirectionDictionary.py
The program will use a dictionary to represent the possible exits from a location in an adventure game.
There is an array containing the directions and descriptions. It uses nested IF and WHILE statements
to handle the user input direction. If the direction is valid, it prints the direction and description
to the screen. If it is invalid, it continues to ask the user for valid input or to exit.

HW7 - TriviaGame.py  and trivia.txt
Trivia.txt contains the text for multiple choice trivia questions.
The trivia is broken down into blocks containing: catrgory, trivia question, possible answers, 
the correct answer, and the explanation.
The program opens that text file and loads the data.
It presents each trivia question to the user, in order, and allows them to answer. 
The user is scored on how many they get correct.
A few function definitions are created to contain repeatedly used code.

HW8 - PlayerClass.py
This program creates a class PLAYER. PLAYER has members: get_inventory, take, drop.
This basic structure could be utilized in a text based game.

HW9 - WeaponClassCrossbow.py
Three classes are defined: weapon, sword, crossbow.
Weapon is the base/parent class. Sword and crossbow derive some characteristics from the weapon class,
and more characteristics are added to them as well.
This base structure could be improved and used in text based games.
