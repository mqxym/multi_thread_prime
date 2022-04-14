#config.py
import sys

class config:
    lower = 0
    upper = 999
    limit = 100 #How many primes you want to calculate

    threadCount = 1

    data = ""
    #Mode 0: No Input
    #Mode 1:Console Input
    #Mode 2 Cmd Arguments input 
    #Mode 3 Load from config
    mode = 1  
    computingPower = 7 #Calculation power increases by 16

    logOutput = 0
    repeatInput = 1

    def help (self):
        print(".thread <val> to change ThreadCount")
        print(".thread <val> to change ThreadCount")
        print(".thread <val> to change ThreadCount")
        print(".thread <val> to change ThreadCount")

    def check (self):
        if self.lower > self.upper:
            print("The lower value is higher than the upper value")
            return False
        if self.lower < 0:
            print("Lower value can't be lower than 0")
            return False
        if self.limit < 1:
            print("Limit must be higher than 0")
            return False
        if self.threadCount > 64:
            self.threadCount = 64
            print("64 Threads is maximum")
        if self.threadCount < 1:
            print("Thread count cant be lower than 1")
            return False
        if self.limit < self.threadCount:
            print("Limit cant be smaller than threadCount")
            return False
        if self.mode < 0 or self.mode > 3:
            print("Mode must be between 0 and 3")
            return False
        if self.computingPower > 8 or self.computingPower < 1:
            print("Computing power must be between 1 and 8")
            return False
        if self.logOutput != 1 or self.logOutput !=0:
            print("Logmode must be 1 or 0")
    
    def setConfig (self,input):
        if input[0] == ".":
            command,value = input.split(" ")
            match command:
                case ".threads":
                    self.threadCount = int(value)
                case ".exit":
                    sys.exit()
                case ".cp":
                    self.computingPower = int(value)
                case ".up":
                    self.upper = int(value)
                case ".low":
                    self.lower = int(value)
                case ".log":
                    self.logOutput = int (value)
                
        else:
            self.data = input