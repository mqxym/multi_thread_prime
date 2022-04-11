import sys
import copy
from threading import Thread

#Idea: write output to file
#Idea create a satus 
#use a logarigthmic scale for thread creation


lower = 10000
upper = 20000

threadCount = 7

threads = []
results = []


def testInput ():
    if lower > upper:
        sys.exit("lower number is higher than upper number")

    if threadCount > 64 or threadCount < 1:
        sys.exit("Thread counter wrong")

    if (lower <= 0):
        sys.exit("Number can't be lover than 0")

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
    

def checkPrimes(lower, upper, threadID):
    print("Thread start ", lower, " to ", upper," ThreadID: ", threadID, "\n")
    for num in range(lower, upper + 1):  
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                #print("Prime: ",num)
                results.append(num)

    #print("Thread ",threadID ," finished.", )

def main():
    testInput()
    difference = round((upper - lower)/threadCount)

    print("Prime numbers between", lower, "and", upper, "are:")

    for i in range(0, threadCount): 
        threadLow = lower + (difference*i)
        threadUp = lower + (difference * (i+1))
        print("Up, ", threadUp, " Low ", threadLow )
        thread = Thread(target=checkPrimes, args=(threadLow,threadUp,i,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Calculating finished")
    print(quicksort(results))

if __name__ == "__main__":
    main()