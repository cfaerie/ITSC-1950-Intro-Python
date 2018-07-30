#Program Name: Player Class
#Date: 3/4/13
#Developer: ITCS 1950 Friday - Rachel Sanford

#This program will define a class "player" that can carry a limited number of items
#represented by strings


class player(object):
    #Define Class Attributes Name, Max_items, items
##    name = ''
##    max_items = ''
##    items = []
    def __init__(self,name,max_items, items = []):
        print "Hello,",name,"You can carry up to ",max_items,"items.\n"
        print "You start with nothing in your inventory.\n"
        self.max_items = int(max_items)
        self.__items = items

    #Class methods: Inventory(), take(), drop()
    
    def get_inventory(self):
        if self.__items != []:
            print "These are in your inventory: ", self.__items, '\n'
        else:
            print "EMPTY.\n"
        

    def take(self,item):
        item = [item]
        if len(self.__items) < self.max_items:
            self.__items += item
            print "You took a: ", item, '\n'
        else:
            print "You tried to take a ",item
            print "You have too many items to take another!\n"
    

    def drop(self,item):
        if item in self.__items:
            self.__items.remove(item)
            print "You dropped a ", item, '\n'
        else:
            print item," isnt in your inventory!\n"


def main():

    player1 = player('Rachel',4)
    player1.get_inventory()
    player1.take('book')
    player1.take('mouse')
    player1.take('key')
    player1.take('radio')
    player1.get_inventory()
    player1.take('ball')
    player1.get_inventory()
    player1.drop('mouse')
    player1.get_inventory()
    player1.take('ball')
    player1.get_inventory()
    player1.drop('bottle')
    player1.get_inventory()
    

    

main()
