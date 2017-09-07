# Problem Set 4
# Name: Bohdan Drahan 
# Collaborators: 
# Time: 5:00 

from types import*

#
# Problem 1
#


def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    assert type(years) is IntType and years >=0, "years - ValueError"
    assert salary >= 0 and save >= 0 and save <=100 and growthRate >=0 and growthRate <=100, "ValueError"
    ans=[]
    if years == 0:
        print 'you have to work harder than 0 years to have any profit'
        return ans
    for x in range(1, years +1):
        if x == 1:
            f = salary * save * 0.01
        else:
            f = ans[x-2] * (1 + 0.01 * growthRate) + salary * save * 0.01
        ans = ans + [f,]
    return ans

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    
    salary     = 10000
    save       = 11
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    

    salary     = 1321
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    
    salary     = 1500
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

    salary     = 10
    save       = 10
    growthRate = 15
    years      = 10 
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord


#testNestEggFixed()

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    
    assert salary >= 0 and save >= 0 and save <=100, "ValueError"

    
    for x in range(0, len(growthRates) +1):
        if x == 0:
            ans = [] 
        if x == 1:
            f = salary * save * 0.01
        elif x > 1:
            f = ans[x-2] * (1 + 0.01 * growthRates[x-1]) + salary * save * 0.01
        if x == 0:
            continue 
        else: 
            ans = ans + [f,]
    return ans


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    
    salary      = 10
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

    
    salary      = 10000
    save        = 10
    growthRates = [15, 15, 15, 15, 15]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    
    salary      = 10000
    save        = 1
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    
    salary      = 10000
    save        = 100
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

#testNestEggVariable()

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """

    for x in range(len(growthRates)):
        if x == 0:
            f = savings * (1 + 0.01 * growthRates[0]) - expenses
            ans = [f]
        else:
            f = ans[x-1]*(1 + 0.01 * growthRates[x]) - expenses
            ans = ans + [f,]
    return ans

    

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 20000
    savingsRecord = postRetirement(savings, growthRates, expenses)

    print savingsRecord
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 300
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 10
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 100000
    growthRates = [99,1,13,14,14,15,13,100,99,99,99,9910, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 100000
    growthRates = [10,95, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 100
    growthRates = [10, 5, 0, 5, 11]
    expenses    = 1 
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    

#testPostRetirement()


#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    for x in range(0, len(preRetireGrowthRates) +1):
        if x == 0:
            ans = [] 
        if x == 1:
            f = salary * save * 0.01
        elif x > 1:
            f = ans[x-2] * (1 + 0.01 * preRetireGrowthRates[x-1]) + salary * save * 0.01
        if x == 0:
            continue 
        else: 
            ans = ans + [f,]
    savings = ans[-1]
    
    low = 0
    high = savings
    for j in range(0,1000):
        if j == 0:
            expenses = (low + high)/2 
        for x in range(len(postRetireGrowthRates)):
            if x == 0:
                f = savings * (1 + 0.01 * postRetireGrowthRates[0]) - expenses
                ans = [f]
            else:
                f = ans[x-1]*(1 + 0.01 * postRetireGrowthRates[x]) - expenses
                ans = ans + [f,]
        if ans[-1] > epsilon:
            low = expenses
        elif ans[-1] <0:
            high = expenses
        else:
            print 'Bi method. Num. iteration:', j, 'estimate:', expenses, 'zero = ', ans[-1]
            return expenses
        expenses = (low + high)/2
        assert j < 999, 'Iteration count exceeded'
        
         


def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3]
    postRetireGrowthRates = [10,10,10,10,0, 5, 0, 5, 1]
    epsilon               = .0001
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses

    salary                = 10
    save                  = 100 
    preRetireGrowthRates  = [0, 0, 0, 0, 0]
    postRetireGrowthRates = [10, 5, 0, 5, 1,10,10,10,10,10,15,100,100,100]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .00000000001
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses

    salary                = 1
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses

testFindMaxExpenses()
