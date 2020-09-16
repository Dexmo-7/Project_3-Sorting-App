#Sorting module

#Bubble sort
def bubbleSort(list_):
    n = len(list_)
    #through all items
    for item in range(n-1):
        #take the element and compare with the other
        for element in range(n-item-1):
            #if this element is bigger than next then replace the elements 
            if list_[element] > list_[element+1]:
                list_[element], list_[element+1] =  list_[element+1],  list_[element]
    #return sorted list            
    return list_
