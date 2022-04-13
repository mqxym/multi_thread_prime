from concurrent.futures import thread
import sys
from threading import Thread
import lib 
import hashlib


lower = 0
upper = 777
limit = 1000 #How many primes you want to calculate

data = "" #Change Data when you want primes based on data
computingPower = 6 #Every increase is increased by *16

if (len(sys.argv)==2):
    data = sys.argv[1]

threadCount = 4

writeToFile = 1
outputToScreen = 1

if (data):
    hash = hashlib.md5(data.encode())
    hex = hash.hexdigest()
    hex = hex[1:computingPower]
    lower = int(hex,16)
    upper = lower+10000
    limit = 3
    threadCount = 2



threads = []
results = []


def testInput ():
    if lower > upper:
        sys.exit("lower number is higher than upper number")

    if threadCount > 64 or threadCount < 1:
        sys.exit("Thread counter wrong")

    if (lower <= 0):
        sys.exit("Number can't be lover than 0")


def isPrime (num):
# all prime numbers are greater than 1
    if num > 1 and len(results) < limit:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            #print("Prime: ",num)
            results.append(num)


def checkPrimes(array, start, end, threadID):
    #print("Thread start ID: ", threadID, "\n")
    for i in range(start,end):  
        #if threadID == 0:
        #    print((i/end)*100, "%")
        # all prime numbers are greater than 1
        isPrime(array[i])

    #print("Thread ",threadID ," finished.", )


def main():

    print("Prime numbers between", lower, "and", upper, "are:")

    array = lib.shuffleArray(lower, upper)
    difference = round((upper - lower)/threadCount)

    for i in range(threadCount): 
        threadLow= difference*i
        threadUp = difference * (i+1)

        thread = Thread(target=checkPrimes, args=(array,threadLow, threadUp,i))
        
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Calculating finished")
    output = lib.quicksort(results)

    if (outputToScreen):
        print (output)

    if (writeToFile):
        with open('out.txt', 'w') as f:
            for prime in output: 
                write = str(prime) + "\n"
                f.write(write)

if __name__ == "__main__":
    main()