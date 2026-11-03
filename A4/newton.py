#This is an implementation of Newton’s Method to calculate Square Roots
#It is a python port of the LISP implementation described in "Structure and Interpretation of Computer Programs" (https://web.mit.edu/6.001/6.037/sicp.pdf book-page 28) by Abelson/Sussman

def square(x):
    return x*x

def average(x, y):
    return (x+y)/2

def isGoodEnough(guess, x):
    return abs(square(guess) - x) < 0.001

def improve(guess, x):
    return average(guess, x/guess)

def sqrtIter(guess, x):
    if isGoodEnough(guess, x):
        return guess
    else:
        return sqrtIter(improve(guess, x), x)
    
def newton(x):
    return sqrtIter(1.0, x)
    
#if __name__ == "__main__":
#    print(newton(4))
#    print(newton(9))