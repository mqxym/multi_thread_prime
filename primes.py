import sys
import threading
import hashlib
import config

results = []


def shuffleArray(lower, upper):
    array = []
    targetCount = round((upper-lower)/2)
    
    for i in range(targetCount):
        array.append(lower+i)
        array.append(upper-i)
    
    return array

def checkPrimes(array, start, end, limit, threadID):
    print("Thread start ID: ", threadID, " starts calculating")
    global results
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

def threader (lower, upper, limit, threadCount):
    threads = []

    print("Prime numbers between", lower, "and", upper, "are:")
    
    array = shuffleArray(lower, upper)    
    difference = round((upper - lower)/threadCount)

    for i in range(threadCount): 
        threadLow= difference*i
        threadUp = difference * (i+1)

        thread = threading.Thread(target=checkPrimes, args=(array,threadLow, threadUp, limit,i))
        
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Calculating finished")    

def main():
    
    c = config.config()
    c.check()

    global results

    if (c.mode == 1):
        print("Enter Data as Input or type exit")
        c.setConfig(input())
        results = []

    if (len(sys.argv)==2 and c.mode == 2):
        c.data = sys.argv[1]

    if (c.data):
        hash = hashlib.md5(c.data.encode())
        hex = hash.hexdigest()
        hex = hex[1:c.computingPower]
        c.lower = int(hex,16)
        c.upper = c.lower+10000
        c.threadCount = 1
        c.limit = 1

    threader(c.lower, c.upper, c.limit, c.threadCount)

    output = sorted(results)
    
    print (output)

    if (c.logOutput):
        with open('out.txt', 'w') as f:
            for prime in output: 
                write = str(prime) + "\n"
                f.write(write)
    
    if(c.mode == 0 or c.mode == 2 or c.mode == 3):
        sys.exit()

if __name__ == "__main__":
    main()