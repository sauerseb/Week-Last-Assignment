# Evan Sauers
# CIS-125-82A
# Collaborated with Dr.Neumann

import math    # Import Math Programming Library
import time
def subsetI(n,k):
    return math.factorial(n) / (math.factorial(k)* math.factorial(n-k))

def subsetR(n,k):
    if n == k:		#Base Case #1
        return 1
    if k == 0:	    #Base Case #2
        return 1
    else:
        return subsetR(n-1,k-1) + subsetR(n-1,k)  #This is the recursion part


def main():
    n = 52           # Insert number of cards
    k = 13
    looptime = 1

    timeB = time.time()             # Time is in milliseconds 
    for x in range(looptime):       # No magic numbers, instead use looptime
        I = subsetI(n,k)
    timeA = time.time()
    print("I = ",I)
    print("elapsed time: ", timeA-timeB)

    timeB = time.time()
    for x in range(looptime):       
        R = subsetR(n,k)    
    timeA = time.time()
    print("R = ",R)
    print("elapsed time: ", timeA-timeB)
 
if __name__ == "__main__":
    main()

    
