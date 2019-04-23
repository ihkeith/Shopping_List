# A Command Line Shopping List Application

## Background

I am currently working through Team Treehouse's [Learn Python](https://teamtreehouse.com/tracks/learn-python) track. I've been gone through it before, then had to step away for a bit, promptly forgetting most of what I learned, then coming back. This time, I am determined to make it stick. One of the ways they help you do this is by giving you coding projects and suggestions on how to extend the application on your own. This is my version of their command line shopping list application.

## Application Overview

The shopping list app presents the user with a simple menu of choices. The user types a command to execute the command or an item to add to the list. In my extension, they have the option to save their list to a text file in the same directory as the application or to load the previous list. I may use change it to save data using Python's shelve module.

## Their Code

Here is the code as they implemented it. It started out simply and in each subsequent video, we learned new concepts and then implemented them in the code to extend the application. They often mentioned a topic, then gave us a chance to research it and implement it on our own before going over how they did it in the video.

```python

import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                            "Press ENTER to add to the end of the list\n"
                            "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()


def show_list():
    clear_screen()

    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    else:
        add_to_list(new_item)

show_list()
```

## My Code

### Things that I did differently

* Wrapped the main loop into its own function
* Created an option to save the list to a txt file
* An option to load the previously saved list
* Used ```enumerate``` to generate the position for each item on the list

### Things I want to add

* Input validation to prevent duplicate items
* Items should have an optional ammount indicate buying more than one item
* An option to export the list, either through SMS or email (or both!)

## What I learned

* Iterating over a list to extract data or modify its contents
* Using For, While, and If statements
* Try and Except blocks
* Breaking components of a program into seperate functions to reduce code duplication and to all for easier editing
* Writing to a file and pulling information from that file