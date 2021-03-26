"""
Program goals:
3. Pull the values stored at specific index
4. Convert input to INTs
5. Put all actions in a while loop
6. Add and exit option 


"""
import random
myList = []
unique_list = []

def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! let's work with lists")
        print("please choose from the following options.  Type the number of the ")
        choice = input ("""1. Add to a list,
2. Return a value in a list
3. Add a bunch of numbers!
4. Random Search
5. Liner Search
6. sort List
7. print lists
8. Quit """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice =="3":
            randomSearch()
        elif choice -- "4":
            randomSearch()
        elif choice --"5":
            linerSearch ()
        elif choice =="6":
            sortList(myList)
        elif choice == "7":
            printLists()
        else:
                break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append (int(newItem))
    #we need to think about errors!


def addABunch():
    print("We're going to add a bunch of numbers to your list")
    numToAdd = input("How many new integers would you like to add?  ")
    numRange = input ("And how high would you likke these numbers to go?  ")
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
        print ("Your list is complete!")

def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input ("Wanna see your new, sorted list?  Y/N")
    if showMe.lower() =="y":
        print(unique_list)

def randomSearch():
    print("oH IM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])


def linerSearch():
    print ("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?  ")
    for x in range (len(myList)):
        if myList[x] == int(searchValue):
            print ("Your item is at index position {}".format(x))


def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your numberis at index position{}".fomat (mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
        else:
            print ("Your number ins't here!")

def indexValues():
    print ("At what index position do you want to search")
    index = input ("Type and index position here:  ")
    print (myList[int(indexPos)])

def printList():
    if len (unique_list) == 0:
        print(myList)
    else:
        whitchOne = input ("which list do you want to see? Sorted or un-sorted   ")
        if whitchOne.lower() == "sorted":
                           print(unique_list)

if __name__ == "__main__": 
    mainProgram()
