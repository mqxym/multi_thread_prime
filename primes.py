import sys
import threading
import hashlib

lower = 0
upper = 20000
limit = 1000 #How many primes you want to calculate

data = "" #Change Data when you want primes based on data
computingPower = 8 #Every increase is increased by *16

enterData = 0
repeatInput = 1 #If you want to keep inputing data

threadCount = 4

writeToFile = 0
outputToScreen = 1

results = []


def testInput ():
    if lower > upper:
        sys.exit("lower number is higher than upper number")

    if threadCount > 64 or threadCount < 1:
        sys.exit("Thread counter wrong")

    if (lower <= 0):
        sys.exit("Number can't be lover than 0")

def shuffleArray(lower, upper):
    array = []
    targetCount = round((upper-lower)/2)
    
    for i in range(targetCount):
        array.append(lower+i)
        array.append(upper-i)
    
    return array

def checkPrimes(array, start, end, threadID):
    print("Thread start ID: ", threadID, " starts calculating")
    global results,limit
    for i in range(start,end):  
        # all prime numbers are greater than 1
        if(len(results) < limit):
            checkPrime = array[i]
            #Checks if Prime
            for i in range(2, checkPrime):
                if (checkPrime % i) == 0:
                    break
            else:
                results.append(checkPrime)
        else:
            print("Thread ",threadID ," finished.", )
            return


def main():
    global repeatInput

    while(repeatInput):

        threads = []
        global data,lower,upper,threadCount,limit,results

        if (enterData):
            print("Enter Data as Input or type exit")
            data = input()
            if (data == "exit"):
                sys.exit()
            results = []
        else:
            repeatInput = 0

        if (len(sys.argv)==2):
            data = sys.argv[1]

        if (data):
            hash = hashlib.md5(data.encode())
            hex = hash.hexdigest()
            hex = hex[1:computingPower]
            lower = int(hex,16)
            upper = lower+10000
            threadCount = 1
            limit = 1

        print("Prime numbers between", lower, "and", upper, "are:")

        array = shuffleArray(lower, upper)
        difference = round((upper - lower)/threadCount)

        for i in range(threadCount): 
            threadLow= difference*i
            threadUp = difference * (i+1)

            thread = threading.Thread(target=checkPrimes, args=(array,threadLow, threadUp,i))
            
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print("Calculating finished")
        output = sorted(results)

        if (outputToScreen):
            print (output)

        if (writeToFile):
            with open('out.txt', 'w') as f:
                for prime in output: 
                    write = str(prime) + "\n"
                    f.write(write)

if __name__ == "__main__":
    main()