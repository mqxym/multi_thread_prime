import sys
from threading import Thread

#Idea: write output to file
#Idea create a satus 


lower = 5000000
upper = 6000000

threadCount = 7

threads = []


def testInput ():
    if lower > upper:
        sys.exit("lower number is higher than upper number")

    if threadCount > 64 or threadCount < 1:
        sys.exit("Thread counter wrong")

    if (lower <= 0):
        sys.exit("Number can't be lover than 0")

def checkPrimes(lower, upper, threadID):
    print("Thread start ", lower, " to ", upper," ThreadID: ", threadID, "\n")
    for num in range(lower, upper + 1):  
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("Prime: ",num)

    #print("Thread ",threadID ," finished.", )

def main():
    testInput()
    difference = round((upper - lower)/threadCount)

    print("Prime numbers between", lower, "and", upper, "are:")

    for i in range(0, threadCount+1): 
        threadLow = lower + (difference*i)
        threadUp = lower + (difference * (i+1))
        print("Up, ", threadUp, " Low ", threadLow )
        thread = Thread(target=checkPrimes, args=(threadLow,threadUp,i,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Calculatin finished")


if __name__ == "__main__":
    main()