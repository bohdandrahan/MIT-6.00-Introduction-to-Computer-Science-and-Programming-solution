# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: BOHDAN DRAHAN
# Collaborators:
# Time: 8:00
#

import time

SUBJECT_FILENAME = "subjects.txt"
#TEST
SUBJECT_FILENAME_TEST = "subjects_test.txt"

VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).
    inputFile = open(filename)
    subj_dict = dict()
    for line in inputFile:
        line_listed = line.split(',')
        line_listed[1] = int(line_listed[1])
        line_listed[2] = int(line_listed[2].strip('\n'))
        subj_dict[line_listed[0]] = line_listed[1:3]
    return subj_dict

global subjects, subjects_test
subjects = loadSubjects(SUBJECT_FILENAME)
subjects_test = loadSubjects(SUBJECT_FILENAME_TEST)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#TEST
#printSubjects(subjects)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    subjects_copy = dict(subjects)
    room_left = maxWork
    no_room = False 
    best_dict = dict()
    while no_room == False and subjects_copy != dict():
        best = (0, float('inf'))
        i = 0
        for subj_name in subjects_copy:
            if room_left < subjects_copy[subj_name][1]:
                i += 1
                continue
            elif comparator(subjects_copy[subj_name], best):
                best = subjects_copy[subj_name]
                best_subject = subj_name
        if len(subjects_copy) == i:
            no_room = True
        else:
            best_dict[best_subject] = best
            room_left -= best[1]
            del subjects_copy[best_subject]
    return best_dict
    
##TEST
#selected = greedyAdvisor(subjects, 10, cmpRatio)
#print 'GREEDY RATIO' 
#printSubjects(selected)
#print 'GREEDY WORK'
#selected = greedyAdvisor(subjects, 10, cmpWork)
#printSubjects(selected)
#print 'GREEDY VALUE'
#selected = greedyAdvisor(subjects, 10, cmpValue)
#printSubjects(selected)


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#

#TEST
#bru = bruteForceAdvisor(subjects_test, 10)
#printSubjects(bru)
def advisorTime(method):
    """
    Takes a method and test it on different lengh of subjects with a step 10 subj.
    Print how many seconds it took to computate
    """
    subjects_copy = dict()
    n = 0
    print 'Testing the method: ', str(method)
    for subj in subjects:
        n += 1
        subjects_copy[subj] = subjects[subj]

        #step = 10 new subjects
        if n/20*20 == n: 
            start = time.time()
            method(subjects_copy,10)
            finish = time.time()
            time_spent = float(finish - start)
            print "It took {0:.2f} sec to compute dictionary with {1} subject(s)".format(time_spent, len(subjects_copy)) 
            if time_spent > 2:
                print "It took MORE THAN 2 SEC to compute dictionary with {0} subjects".format(len(subjects_copy))
                n = len(subjects_copy)
                break

def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """

    # TODO...

    advisorTime(bruteForceAdvisor)

#WHAT? I HAVE TO WAIT MORE THAN 2 SEC TO COMPUTE DICTIOANRY WITH 220 SUBJECTS!!!
#IM NOT GONNA WAIT THAT LONG!!! THAT IS TOO MUCH!!!!11!!!1!


##TEST
bruteForceTime()



# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
#WHAT? I HAVE TO WAIT MORE THAN 2 SEC TO COMPUTE DICTIOANRY WITH 220 SUBJECTS!!! IM NOT GONNA WAIT THAT LONG!!! THAT IS TOO MUCH!!!!11!!!1! 
#
#I mean it's not that bad, If you can wait around 45 sec to compute the whole subjects list the brute force algorithm is OK solution. 
#I've spent around 4 hours to write a code for dynamic programming solution. So 4 hours/ 45 sec = 320 times. Lets assume that time of every human in the world is equaly important(which is not true)
#Its means if this program will be used more than 320 times it is worht to spent 4 hours for optimazation 

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    i = 0
    value = list()
    work = list()
    id_key = dict()

    for key in subjects:
        id_key[i] = key
        value.append(subjects[key][0])
        work.append(subjects[key][1])
        i += 1

    mem = dict()
    result_keys = dict()
    result_value = 0

    result_value, result_keys = dpAdHelper(value, work, i - 1, maxWork, mem)
    result_list = dict()
    for key in result_keys:
        result_list[id_key[key]] = (value[key], work[key])
    return result_list

def dpAdHelper(value, work, i , room_left, mem):
    try: return mem[(i, room_left)]
    except KeyError:
        if i == 0:
            if work[i] <= room_left: 
                mem[(i,room_left)] = value[i],[i]
                return value[i], [i] 
            else:
                mem[(i, room_left)] = 0, []
                return 0, []
    dont_take_i, result_keys = dpAdHelper(value,work, i-1, room_left, mem)
    if work[i] > room_left:
        mem[(i, room_left)] = dont_take_i, result_keys
        return dont_take_i, result_keys
    else:
        take_i, result_keys_temp = dpAdHelper(value, work, i - 1, room_left - work[i], mem)
        take_i += value[i]

    if take_i > dont_take_i:
        i_value = take_i
        result_keys = [i] + result_keys_temp
    else: 
        i_value = dont_take_i

    mem[(i, room_left)] = i_value, result_keys
    return i_value, result_keys
    
##TEST
#work_test = 10
#selected = greedyAdvisor(subjects_test, work_test, cmpRatio)
#print 'GREEDY RATIO' 
#printSubjects(selected)
#print 'GREEDY WORK'
#selected = greedyAdvisor(subjects_test, work_test, cmpWork)
#printSubjects(selected)
#print 'GREEDY VALUE'
#selected = greedyAdvisor(subjects_test, work_test, cmpValue)
#printSubjects(selected)
#selected = dpAdvisor(subjects_test, work_test)
#print 'DYNAMIC PROG'
#printSubjects(selected)
#bru = bruteForceAdvisor(subjects_test, work_test)
#print 'BRUTE FORCE'
#printSubjects(bru)

#
# Problem 5: Performance Comparison
#

def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    advisorTime(dpAdvisor)

#TEST
dpTime()


# Problem 5 Observations # ====================== # # TODO: write here your observations regarding dpAdvisor's performance and # how its performance compares to that of bruteForceAdvisor.
#It is superfast and super efficient. It took 0.01 sec to copmute the whole subjects list. 
