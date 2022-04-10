import sys
from threading import Thread

lower = 1
upper = 400

threads_count = 7

threads = []


def testInput ():
    if lower > upper:
        sys.exit("lower number is higher than upper number")

    if threads_count > 64 or threads_count < 1:
        sys.exit("Thread counter wrong")

    if (lower <= 0):
        sys.exit("Number can't be lover than 0")

def checkPrimes(lower, upper, threadID):
    print("Thread from ", lower, " to ", upper," ThreadID: ", threadID, "\n")
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
    difference = round((upper - lower)/threads_count)

    print("Prime numbers between", lower, "and", upper, "are:")

    for i in range(0, threads_count+1): 
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