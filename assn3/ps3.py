# Problem Set 4
# Name: Bohdan Drahan
# Time: 

import string

# Problem 1

def countSubStringMatch(target,key):
    count = 0
    for x in range(0,len(target)-len(key)+1):
        if key == target[x:x+len(key)]:
            count += 1
    return count

def countSubStringMatchRecursive(target,key):
    if string.find(target,key) == -1:
        return 0
    else: return countSubStringMatchRecursive(target[string.find(target,key)+1:],key)+1

            
# Problem 2
def subStringMatchExact(target,key):
    count = 0
    result =() 
    for x in range(0,len(target)-len(key)+1):
        if key == target[x:x+len(key)]:
            count += 1
            result=result+(x,)
    return result
     

# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3
# Problem 3

def constrainedMatchPair(firstMatch,secondMatch,length):
    ans = ()
    for x in range(0,len(firstMatch)):
        for y in range(0,len(secondMatch)):
            if int(firstMatch[x]+length) == int(secondMatch[y]):
                ans=ans+(firstMatch[x],)
    return ans
    print 'ans',ans

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
    
# Problem 4
def subStringMatchExactlyOneSub(target,key):
    x = subStringMatchOneSub(key,target)
    y = subStringMatchExact(target,key)
    return tuple(set(x)-set(y))

    
    
