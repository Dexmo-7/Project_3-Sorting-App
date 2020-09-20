#Insertionsort
def insertionSort(list_):
    #through item 1 to len(list_)
    for item in range(1, len(list_)):
        key = list_[item]
        #Move elements of list_[0..i-1], that are
        #greater than key, to one position ahead
        #of their current position
        element = item-1
        while element >= 0 and key < list_[element]:
            list_[element + 1] = list_[element]
            element -= 1
        list_[element + 1] = key
    #return sorted list_
    return list_
