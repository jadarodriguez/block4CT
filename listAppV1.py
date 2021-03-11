"""
Program goals:
3. Pull the values stored at specific index
4. Convert input to INTs
5. Put all actions in a while loop
6. Add and exit option 


"""

def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! let's work with lists")
        print("please choose from the following options.  Type the number of choice")
        choice = input("1. Add to list, 2. Return a value at a list   ")
        if choice == "1":
            addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myLIst.append (int(newItem))
    #we neeed to think about errors!
    

def indexValues():
    print ("At what index position do you want to search")
    index = input ("Type and index position here:  ")
    print (myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()
