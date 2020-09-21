#quickSort
#from page geeksforgeeks.org

def partition(list_, first, last):
    i = (first-1) #index of smaller element
    pivot = list_[last]
    
    for j in range(first, last):
        #if current element is smaller than or equal to pivot
        if list_[j] <= pivot:
            #increment index of smaller element
            i += 1
            list_[i], list_[j] = list_[j], list_[i]
        
    list_[i+1], list_[last] = list_[last], list_[i+1]
    return i+1

#main function
#list_ - list to be sorted
#first - starting index
#last - ending index

def quickSort(list_, first, last):
    if len(list_) == 1:
        return list_
    if first < last:
        #part is partitioning first, list_[p] is now at right place
        part = partition(list_, first, last)
        
        #separately sort elements before partition and after partition
        quickSort(list_, first, part-1)
        quickSort(list_, part+1, last)
        return list_