# The Elevator Simulator.
# Justin T. Dejesus - 08/12/2014
# Simulate M elevators moving aross N floors
# show this as a 2 dimentional list
# a list of lists of elevator objects
# I'll need to define an elevator class
# including __repr__() and possibly an exception handler helper class
# I will need a function that starts the program
# As well as a frame class to display the "elevator bank"
# in a simple GUI format. Everything should run in a while loop
# that endlessly picks up patrons in this hypothetical building
# so implement a timing function as well that randomly shows patrons
# because of this the M lists will all be M + 1 and that final object
# is persons on that floor.
# elevators have a floor attribute. which is what list they should be assigned
# and a bank attribute. which is what index they are assigned to.
# elevators cannot leave their assign bank and begin at the N[-1] list
# or the ground floor
# elevators should also have a weight attribute and not add more patrons
# than it's weight.

class Elevator:
    ''' defines elevator object'''

    def __init__(self, floor, bank, weight):
        #which list - N
        self.floor = floor
        
        # which index - M
        self.bank = bank

        # what weight - O
        self.weight = weight

    # set various attributes
    # this isn't working. think about it.

    def setFloor(self, newfloor):
        # When you move a new floor
        self.floor = newfloor
   
    def setBank(self, newbank):
        # this can't change.
        # but I suppose if it was a wonkavator this would work..
        self.bank = newbank
        

    def setWeight(self, newweight):
        # make an exception handler so it cant go below zero
        # if zero, cannot pick up people
        self.weight = newweight

    # return various attributes as needed

    def getFloor(self):
        return self.floor

    def getBank(self):
        return self.bank

    def getWeight(self):
        return self.weight


    def __repr__(self):
        # complete repr
        return ("Floor: {}\nBank: {}\nWeight: {}\n".format(self.getFloor(),
                                                           self.getBank(),
                                                           self.getWeight()))
# test lines for the object class

MyEla = Elevator(10, 10, 10)

print(MyEla)

MyEla.setFloor(2)
print(MyEla)
MyEla.setBank(4)
print(MyEla)
MyEla.setWeight(6)
print(MyEla)
