#Sorting app
#First user provide numbers for sort (or generator do this)
#Secondly user choosing one of the sort method
#Finally we obtain the result
#User can use another method or provide new numbers
from bubble import bubbleSort
from insert import insertionSort
import random

def viewer(valueList):
    print("\n------Sorted list------")
    print(valueList)
    print("-----------------------\n\n")

#Starting conditions
prog_set = True
valueList = []

while prog_set:
    #cleaning the valueList
    valueList.clear()
    #substart condition
    subprog_set = True
    
    print("""Sorting app.\n
        What do you want to do?\n
        1. Enter my values (please use comma as separator)
        2. Generate 10 random numbers
        3. Exit""")

    remote_control = input()
    
    if remote_control == "1":
        number_of_el = int(input("How many elements?"))
        for item in range(number_of_el):
            valueList.append(int(input(f"Please enter the {item+1} number to sort: ")))
    elif remote_control == "2":
        for item in range(10):
            rnd_nmb = random.randint(0,100)
            valueList.append(rnd_nmb)
    elif remote_control == "3":
        prog_set = False
        subprog_set = False
    else:
        subprog_set = False
    while subprog_set:
        print("""Choose the sort method:\n
        1. Bubble sort
        2. Insert sort
        3. Quick sort
        4. Exit to menu
        5. EXIT\n
        """)
        mini_remote_control = input()
        if mini_remote_control == "4":
            subprog_set = False
        elif mini_remote_control == "1":
            valueList = bubbleSort(valueList)
            viewer(valueList)
        elif mini_remote_control == "2":
            valueList = insertionSort(valueList)
            viewer(valueList)
        elif mini_remote_control == "3":
            #valueList = quickSort(valueList)
            #viewer(valueList)
            pass
        elif mini_remote_control == "5":
            subprog_set = False
            prog_set = False
        else:
            print("\n")
        print("Continue? \n1. No \n2. Yes")
        remote_control = input()
        if remote_control == "1":
            subprog_set = False
            prog_set = False
        elif remote_control == "2":
            print("\n")
