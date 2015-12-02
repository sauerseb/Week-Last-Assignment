# Evan Sauers
# CIS-125-82A
# Collaborated with Dr.Neumann

def gCd(x, y):
    print("X = ",x, "Y = ",y)
    if y == 0:
        return x
    else:
        return gCd(y, x%y)   # Return out GCD
        
    
def main():
    x = 252       # Choose two numbers, these will be our x and y
    y = 105
    print("GCD of",x,",",y,"=",gCd(x,y))
    
if __name__ == "__main__":
    main()
