# Problem Set 1
# Name: Bohdan Drahan
#

#Problem 2.
#Write a program that computes the sum of the logarithms of all the primes from 2 to some number n, and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities. Test this for different values of n.

import math


cand = 3
sumLogPrime = math.log(2) 
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
        sumLogPrime = sumLogPrime + math.log(prime)
        ratio = prime/sumLogPrime
        print sumLogPrime, ratio
        cand += 2
    else: isPrime = False
print("The %sth prime number = %s, The sum of ln primes = %s, ratio = %s"%(whatnum,prime,sumLogPrime,ratio))
