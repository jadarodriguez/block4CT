"""
Program goals:
1. Add items to a list (int)
2. offer the user a choice of actions
3. Pull the values stored at specific index
4. Convert input to INTs


"""

def mainProgram():
    myList = []
    print("Hello, there! let's work with lists")
    print("please choose from the following options.  Type the number of choice")
    choice = input("1. Add to list, 2. Return a value at a list   ")
    if choice == "1":
        addToList()
        elif choice == "2":
            indexValues()

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myLIst.append (int(newItem))
    #we neeed to think about errors!

def indexValues():




if __name__ =="__main__":
    mainProgram()
