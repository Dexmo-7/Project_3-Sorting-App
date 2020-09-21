#Sorting app
#First user provide numbers for sort (or generator do this)
#Secondly user choosing one of the sort method
#Finally we obtain the result
#User can use another method or provide new numbers
from bubble import bubbleSort
from insert import insertionSort
from quick import *
import random
import timeit

#subprogram which view the final list
def viewer(valueList):
    print("\n------Sorted list------")
    print(valueList)
    print("-----------------------\n\n")
#subprogram for subloop if "1" then quit the program
def set_continue(mini_remote_control):
    mini_remote_control = input("Continue? \n1. No \nANY NUM. Yes\n")
    return mini_remote_control

#Starting conditions
prog_set = True
valueList = []
mini_remote_control = 0

while prog_set:
    #cleaning the valueList
    valueList.clear()
    #story telling
    print("""           Sorting app.\n
        What do you want to do?\n
        1. Enter my values (please use comma as separator)
        2. Generate 10 random numbers
        3. Exit""")
    #variable for user communication
    remote_control = input()
    #Enter the values
    if remote_control == "1":
        number_of_el = int(input("\nHow many elements?\n"))
        for item in range(number_of_el):
            valueList.append(int(input(f"Please enter the {item+1} number to sort: ")))
        subprog_set = True
    #Generate 10 random values
    elif remote_control == "2":
        for item in range(10):
            rnd_nmb = random.randint(0,100)
            valueList.append(rnd_nmb)
        subprog_set = True
    #Quit the program
    elif remote_control == "3":
        prog_set = False
        subprog_set = False
    #if none of above numbers were entered then continue the main loop
    else:
        subprog_set = False
    #subloop with sort methods
    while subprog_set:
        #storytelling
        print("""\nChoose the sort method:\n
        1. Bubble sort
        2. Insert sort
        3. Quick sort
        4. Exit to menu
        5. EXIT\n
        """)
        remote_control = input()
        #exit to menu
        if remote_control == "4":
            subprog_set = False
        #bubbleSort
        elif remote_control == "1":
            valueList = bubbleSort(valueList)
            viewer(valueList)
            mini_remote_control = set_continue(mini_remote_control)
        #insertionSort
        elif remote_control == "2":
            valueList = insertionSort(valueList)
            viewer(valueList)
            mini_remote_control = set_continue(mini_remote_control)
        #quickSort
        elif remote_control == "3":
            last = len(valueList)-1
            valueList = quickSort(valueList, 0, last)
            viewer(valueList)
            mini_remote_control = set_continue(mini_remote_control)
        #quit from program
        elif remote_control == "5":
            subprog_set = False
            prog_set = False
        #if none of above were entered then continue the subloop
        else:
            print("\n")
        #if mini_remote_control == "1" then quit the program
        if mini_remote_control == "1":
            subprog_set = False
            prog_set = False
