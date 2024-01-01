import hashlib
import sys

data = "What about"	

def main():
	global data
	
	computingPower = 7
	
	if (len(sys.argv)==2):
		data = sys.argv[1]
	
	hash = hashlib.md5(data.encode())
	hex = hash.hexdigest()
	hex = hex[1:computingPower]
	lower = int(hex,16)
	upper = lower+10000
	
	for i in range(lower,upper):  
		checkPrime = i
		for j in range(2, checkPrime):
			if (checkPrime % j) == 0:
				break
		else:
			print('Prime for \'', data , '\' is ', checkPrime)
			return

if __name__ == "__main__":
	main()
