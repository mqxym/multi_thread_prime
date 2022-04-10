import sys

lower = 1234567
upper = 1235000

threads = 4

if lower > upper:
    sys.exit("lower number is higher than upper number")

if threads > 64 or threads < 1:
    sys.exit("Thread counter wrong")

if (lower < 0):
    sys.exit("Number can't be lover than 0")


def main():
    print("Prime numbers between", lower, "and", upper, "are:")
    checkPrimes(lower, upper)
    


def checkPrimes(lower, upper):
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == "__main__":
    main()