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

import tkinter as tk
##import tkinter.scrolledtext as tkst

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
##        return ("Floor: {}\nBank: {}\nWeight: {}\n".format(self.getFloor(),
##                                                           self.getBank(),
##                                                           self.getWeight()))
        return("E")

class DisplayElevator(tk.Frame):
    '''displays and updates the Building on the display'''

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        canvas = tk.Canvas(self, width = 800, height = 500)
        canvas.pack(side = "top", fill = "both", expand = True)
        canvas_id = canvas.create_text(10, 10, anchor = "nw")
        canvas.itemconfig(canvas_id, text = printBuilding(MyBuilding))
        canvas.insert(canvas_id, 12, printBuilding(MyBuilding))


def printBuilding(building):
    '''print the building as needed'''
    
    thebuilding = ""
    
    for floor in building:
        for bank in floor:
            thebuilding += str(bank).ljust(2) + " "
        thebuilding += "\n"

    return thebuilding

# write a function to load and run the program.
# everything should be in this init function to run

def myInit():
    '''initialize the program'''
    global MyBuilding

    print("Welcome to elevator simulator!\n\n")

    MyFloor = int(input("How many floors does this building have?\n\n"))

    MyBanks = int(input("How many elevators does this building have?\n\n"))
    
    MyWeight = int(input("What is the maximum number of patrons in each elevator?\n\n"))

    MyElevators = Elevator(MyFloor, MyBanks, MyWeight)

    cable = "|"

    blank = ""

    patrons = 0
    # This merits some explanation:
    # append the the floor number to each element if it is the firstlist but not the last element.
    # append a class object (they are all the same initially) to each element of the last list
    # or a 0 (patrons on each floor) if its the final element of each list
    # or a | representing a cable if none of those are not the true condition
    MyBuilding = [[blank if floor == 0 and bank == MyElevators.getBank() 
                   else bank + 1 if floor == 0
                   else MyElevators if floor == MyElevators.getFloor() and bank != MyElevators.getBank()
                   else patrons if bank == MyElevators.getBank()
                   else cable for bank in range(0, MyElevators.getBank() + 1)] for floor in range(0, MyElevators.getFloor() + 1)]

    # variables and method for Tkinter
    EleWin = tk.Tk()
    DisplayElevator(EleWin).pack(side = "top", fill = "both", expand = True)
    EleWin.mainloop()
##    EleWin = tk.Tk()
##    EleFrame = tk.Frame(master = EleWin, bg = '#808000')
##
##    EleFrame.pack(fill = 'both', expand = 'yes')
##
##    editArea = tkst.ScrolledText(master = EleFrame,
##                                 wrap = tk.WORD,
##                                 width = 3 * len(MyBuilding[0]),
##                                 height = 1 * len(MyBuilding))
##
##    editArea.pack(padx = 10,
##                  pady = 10,
##                  fill = tk.BOTH,
##                  expand = True)
##
##    # print text into tk frame
##    editArea.insert(tk.INSERT, printBuilding(MyBuilding))
    
myInit()





    
