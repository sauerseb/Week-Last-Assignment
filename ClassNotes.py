# Evan Sauers
# CIS-125-82A
# Collaborated with Dr.Neumann

def moveTower(n, source, dest, temp):
    if n==1:
        print("Move disk from ", source, "to", dest +".")
    else:
         moveTowe(n-1,source, temp, dest)
         moveTower(1, source, dest, temp)
         moveTower(n-1, temp, dest, source)


def hanoi(n):
    moveTower(n, "A","B","C")
    
    
def main():
    d = eval(input("Please enter number of discs: "))
    hanoi(d)
    
if__name__=="__main__"
    main()