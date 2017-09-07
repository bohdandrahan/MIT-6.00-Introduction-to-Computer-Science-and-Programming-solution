# Problem Set 1
# Name: Bohdan Drahan
#

#Problem 1.
#Write a program that computes and prints the 1000th prime number. 

cand = 3
i = 2
whatnum = int(raw_input('Enter the rank of prime number you are looking for:'))
while i !=whatnum + 1:
    #Check cand for prime
    for d in range(2, cand):
        if cand%d == 0:
            print cand, 'not a prime'
            cand +=2
            break
        else: d +=1
    if d == cand:
        isPrime = True
        print cand,' is a prime, index =', i
        i += 1
        prime = cand
        cand += 2
    else: isPrime = False
print("The %sth prime number = %s"%(whatnum, prime))
