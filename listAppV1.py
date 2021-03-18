"""
Program goals:
3. Pull the values stored at specific index
4. Convert input to INTs
5. Put all actions in a while loop
6. Add and exit option 


"""
import random
myList = []
def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! let's work with lists")
        print("please choose from the following options.  Type the number of the 
              choice = input ("""1. Add to a list,
2. Return a value in a list
3. Add a bunch of numbers!
4. Random search
5. Print List
6. Quit """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice =="3":
                randomSearch()
            elif choice -- "4":
                randomSearch()
            elif choice --"5":
                print (myList)
            else:
                break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myLIst.append (int(newItem))
    #we need to think about errors!


def addABunch():
    print("We're going to add a bunch of numbers to your list")
    numToAdd = input("How many new integers would you like to add?  ")
    numRange = input ("And how high would you likke these numbers to go?  ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
        print ("Your list is complete!")

def randomSearch():
    print("oH IM sO rAnDom!!!")
    print myList[random.randint(0, len(myList)-1)])


def linerSearch():
    print ("We're going to go through this list one item at a time!")
    

def indexValues():
    print ("At what index position do you want to search")
    index = input ("Type and index position here:  ")
    print (myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()
