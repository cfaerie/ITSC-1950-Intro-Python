class weapon (object):
    def __init__(self,damage=0):
        self.damage = damage
    def __str__(self):
        rep = str(self.damage)
        return rep

class sword(weapon):
    """Derived class of weapon"""
    def swing(self):
        print ("Swing does", self.damage ,"damage")

class crossbow(weapon):
    def __init__(self,arrow):
        self.arrow = arrow
##        if arrow == 1:
##            print ("Crossbow is loaded.\n")
##        elif arrow == 0:
##            print ("This is an unloaded crossbow.\n")
##        elif arrow > 1:
##            print ("You can only load one arrow at a time. Let me help you.")
##            arrow = 1
##            print ("Alright, one arrow is loaded.\n")
##        else:
##            print ("Invalid response. You'll have to load an arrow later.\n")
##            arrow = 0
    def is_loaded(self):
        if self.arrow == 0:
            print ("Crossbow isn't loaded. Load an arrow.\n")
        elif self.arrow == 1:
            print ("Crossbow is locked and loaded. Fire away!\n")


    def fire(self):
        if self.arrow == 1:
            self.arrow -= 1
            print ("You shot an arrow!\n")
        elif self.arrow == 0:
            print ("There's nothing in the chamber to shoot.\n")

    def reload(self):
        if self.arrow < 1:
            self.arrow += 1
            print ("Loading a new arrow.\n")
        else:
            print ("You already have an arrow in the chamber. Fire it!\n")

def main():
    crossbow1 = crossbow(0)
    crossbow2 = crossbow(1)
    crossbow3 = crossbow(3)
    crossbow2.is_loaded()
    crossbow2.fire()
    crossbow2.is_loaded()
    crossbow2.reload()


main()
