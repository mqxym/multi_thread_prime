import threading

results = []
lower = 1234000
upper = 1245000
limit = 10000
threadCount = 6

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
	global results, lower,upper, limit, threadCount

	threader(lower, upper, limit, threadCount)
	
	output = sorted(results)
	
	print (output)
	

if __name__ == "__main__":
    main()
