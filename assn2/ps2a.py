# Problem Set 2 (part I)
# Name: Bohdan Drahan
# Time: 4:00

# Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity.

#6a+9b+20c=n

import math

def solveMcNug(a,b,c):
    largestNum=0
    for n in range(0,200):
        print n
        solutionFound = False
        for indexa in range(0, int(n/a) *(n/b)*(n/c)+1): 
        #indexa=0
        #while indexa <= float(n/a)+0.00001: # fixing float/int compressing
            for indexb in range(0, (n - indexa*a)/b +1):
            #indexb=0
            #while indexb <=(n/a-indexa*a+1):
                indexc =(n - indexa*a - indexb*b)/c
                if  indexc<0:
                    continue 
                elif n ==(a*indexa+b*indexb+c*indexc):
                    print(indexa,a,indexb,b,indexc,c,n)
                    solutionFound = True
        if solutionFound == False:
            largestNum = n
            print 'No solution'
    print 'Largest number of McNuggets that cannot be bought in exact quantity:%s'%largestNum
    
a=6
b=9
c=20
solveMcNug(a,b,c)
