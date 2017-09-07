# Problem Set 2 (part II)
# Name: Bohdan Drahan
# Time: 0:30 


def solveMcNug(a,b,c):
    a = int(raw_input('Enter a:'))
    b = int(raw_input('Enter b:'))
    c = int(raw_input('Enter c:'))
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
    print 'Given package sizes {}, {}, and {} , the largest number of McNuggets that cannot be bought in exact quantity is:{}'.format(a,b,c,largestNum)
    
solveMcNug(a,b,c)
