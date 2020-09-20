#Sorting app
#First user provide numbers for sort (or generator do this)
#Secondly user choosing one of the sort method
#Finally we obtain the result
#User can use another method or provide new numbers
import bubble
import insert

#Starting conditions
prog_set = True

while prog_set:
    subprog_set = True
    print("""Sorting app.\n
        What do you want to do?\n
        1. Enter my values (please use comma as separator)\n
        2. Generate random numbers\n
        3. Exit""")

    remote_control = input()
    
    if remote_control == "1":
        pass
    elif remote_control == "2":
        pass
    elif remote_control == "3":
        prog_set = False
    else:
        pass
    while subprog_set:
        print("""Choose the sort method:\n
            1. Bubble sort\n
            2. Insert sort\n
            3. Quick sort\n
            4. Exit to menu\n
            """)
        mini_remote_control = input()
        if mini_remote_control == "4":
            subprog_set = False
        elif mini_remote_control == "1":
            #bubbleSort()
            pass
        elif mini_remote_control == "2":
            #insertSort()
            pass
        elif mini_remote_control == "3":
            #quickSort()
            pass
        else:
            print("\n")
