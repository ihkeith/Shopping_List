import os


# Make a list to hold our items
shopping_list = []


# Funtion Definitions
def showHelp():
    clearScreen()
    print("Welcome to the Shopping List. What shall we get today?")
    print("Enter HELP to see this screen again")
    print("Enter SHOW to see the current list")
    print("Enter LOAD to load the previous list")
    print("Enter SAVE to save the current list")
    print("Enter DONE to exit the program")


def clearScreen():
    os.system("cls" if os.name == 'nt' else 'clear')


def showList():
    clearScreen()
    print("Here's your list:")

    for index, item in enumerate(shopping_list, start = 1):
        print("{}. {}".format(index, item))

    print("-" * 15)

def addItem(newItem):
    clearScreen()

    if len(shopping_list): # if there is something in the shopping list
        position = input("Where should I add {}? \n"
                "Press ENTER to add to the end of the list\n"
                ">>> ".format(newItem))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, newItem)
    else:
        shopping_list.append(newItem)
    
    showList()
    print("{} was added to the list.".format(newItem))

def removeItem():
    showList()
    
    removed_item = input("What would you like to remove?\n"
            ">>> ")
    try:
        shopping_list.remove(removed_item)
    except ValueError:
        pass
    
    showList()

    print("{} was successfully removed from the list.".format(removed_item))

def saveList():
    file = open('shopping_list.txt', 'w', newline='\r\n')
    for item in shopping_list:
        file.write(item + '\n')
    print("Your list was sucessfully saved.")

    file.close()


def loadList():
    file = open('shopping_list.txt', 'r', newline='\r\n').read().splitlines()
    for item in file:
       shopping_list.append(item)
    
    # I need a validation to prevent adding duplicate items!

    showList()


# Main Loop for the Application
def main():
    showHelp()
    while True:
        newItem = input(">>>  ")
        if newItem.upper() == 'HELP':
            showHelp()
            continue
        elif newItem.upper() == 'SHOW':
            showList()
            continue
        elif newItem.upper() == 'DONE':
            break
        elif newItem.upper() == 'SAVE':
            saveList()
            continue
        elif newItem.upper() == 'LOAD':
            loadList()
            continue
        elif newItem.upper() == 'REMOVE':
            removeItem()
            continue
        addItem(newItem)
    
    showList()


# And. here. we. go !
main()
