#Program Name: Direction Dictionary
#Developer: ITCS 1950 Friday Section -- Rachel Sanford
#Date: 2/14/13

#This program will use a dictionary to represent the possible exits
#from a location in an adventure game.

direction = {"north":"That direction leads to the kitchen",
             "south":"That direction leads to the dining room",
             "east":"That direction leads to the entry",
             "west":"That direction leads to the living room"}
command = ''
print """Welcome to the Direction Dictionary Simulator.
With this program, we've created a basic direction interface for a text based game.

The program will recieve and interpret direction input of North, South, East,
and West. (The direction names may be lowercase)
'q' is to quit
All other input will be considered invalid."""

while command == '' or command.lower() in direction:
    command = raw_input("Pick a direction or enter 'q' to exit: ")
    command = command.lower()
    if command not in direction:
        if command != 'q':
            print"Invalid response."
            command = raw_input("Pick a direction or enter 'q' to exit: ")
            while command not in direction:
                command = raw_input("Pick a direction or enter 'q' to exit: ")
                if command == 'q':
                    print "Thanks for playing!"
                    raw_input()
                    break
                
        
        else:
            print "Thanks for playing!"
            raw_input()
            break
        
    if command in direction:
        print direction[command]
    
