#lib.py
import copy

def splitList(a_list):
    half = len(a_list)//2
    return a_list[:half]

def swap(arr, pos1, pos2):
    tmp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = tmp
    return arr
 
def quicksort(arr):
    p = arr[len(arr)-1] # p ist letzes Element im Array
    z = 0 #Zähler für Position im Array
    for i in range(len(arr)):
        # print(arr[i], p, z)
        if arr[i] <= p:
            arr = swap(arr, i, z)
            z = z+1     
    
    arr1 = arr[0:z-1] # Erster Teil des Arrays ohne p
    arr2 = arr[z:len(arr)] #Zweiter Teil des Arrays ohne p
    if len(arr1) > 1:
        arr1 = quicksort(arr1)
    if len(arr2) > 1:
        arr2 = quicksort(arr2)
        
    # Sortiertes Array zusammensetzen aus arr1, p, arr2
    arr0 = copy.deepcopy(arr1)
    arr0.append(p)
    arr0.extend(arr2)
    return(arr0)

# create a list with alternating high low values
def shuffleArray(lower, upper):
    array = []
    targetCount = round((upper-lower)/2)
    
    for i in range(targetCount):
        array.append(lower+i)
        array.append(upper-i)
    
    return array