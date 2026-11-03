### Assignment hop_decorator ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################

#Task 1: Newton Method using inner functions
#In this task you shall make use of inner functions.
#Refactor the code provided in newton.py such that the functions 'isGoodEnough', 'improve' and 'sqrtIter' are inner functions of function 'newton'.
#Get rid of unnecessary parameters (remember that the outer function defines a scope that spans also over the inner functions)
#Do not simplify the code otherwise (e.g., do not get rid of the functions 'square' or 'average')

def square(x):
    return x*x

def average(x, y):
    return (x+y)/2
    
def newton(x):
    def isGoodEnough(guess):
        return abs(square(guess) - x) < 0.001

    def improve(guess):
        return average(guess, x/guess)

    def sqrtIter(guess):
        if isGoodEnough(guess):
            return guess
        else:
            return sqrtIter(improve(guess))

    return sqrtIter(1.0)
  

##########################################################################

#Task 2: Newton Method Simplified and Pythonified
#Simplify the code provided in file newton.py
#Try a python-style approach, but keep the basic mode of operation (it shall still be an iterative improvement; do not simply use something like math.sqrt(x) or x ** 0.5)

def newtonPy(x):
    guess = 1.0
    while abs(guess*guess - x) >= 0.001:
        guess = (guess + x/guess)/2
    return guess
  

##########################################################################

#Task 3: log-Decorator
def log(f):
    def wrapper(*args):
        result = f(*args)
        print(f"@log: {f.__name__}({','.join(map(str, args))}) -> {result}")
        return result
    return wrapper

#Write a decorator 'log' that logs the invokation of functions (with parameters and result) as follows:

#Example: The following code
'''
@log
def helperfunction(a, b):
  return a+b

helperfunction(1,2)
'''
#shall provide the following output (Note: make sure that the returned value of the decorated function is not lost; see last output line!):
'''
@log: helperfunction(1,2) -> 3
'''

##########################################################################

# Task 4: time-Decorator
# Get familiar with time.time() and use it to write a decorator 'timeMe' that logs the time it takes to execute a decorated function.
# Properly format your output
# Important: your decorator shall support functions with an arbitrary number of arguments (but no keyword-arguments)

import time

def timeMe(f):
    def wrapper(*args):
        start = time.time()
        result = f(*args)
        print(f"@timeMe: {(time.time() - start)*1000:.2f} milliseconds")
        return result
    return wrapper

#The following code:
'''
@timeMe
def testFunctionTime():
  sum = 0
  for i in range(10000):
    sum += i

@timeMe
def testFunctionTime2(t):
  time.sleep(t)

@timeMe
def testFunctionTime3(*args):
  s =0
  for a in args:
    s+= a
  time.sleep(s)  

testFunctionTime()
testFunctionTime2(1)
testFunctionTime3(1,2,3)
'''

#shall provide the following output (note that your values will slightly differ):
'''
@timeMe: 0.62 milliseconds
@timeMe: 1001.12 milliseconds
@timeMe: 6001.04 milliseconds
'''

##########################################################################

#Task 5: memoization-Decorator
#Understand the basic idea of Memoization (e.g., https://en.wikipedia.org/wiki/Memoization)
#Write a decorator 'memo' to cache the results of function invocations. 
#It shall work by storing the results of 'expensive' function calls and returning the cached result when the same inputs occur again.
#You can use a dictionary in your decorator to store arg:returnedResult pairs
#Use the fib-function below, which calculates fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...), to test your decorator.
#Note that without the using the decorator already very low numbers (such as fib(35) will take quite a long time.  Can you explain, why this is the case?


def memo(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

# Without memoization, fib repeatedly computes the same subproblems, taking
# exponential time; caching computes each n once, reducing this to linear time.


#calcultes the n-th fibonacci number

@memo
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2) 

#fib(5)
#fib(35)
#list(map(fib, range(20)))


