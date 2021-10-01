Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Successive Approximation
#
#
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.
    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9
    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    polylist = list(poly)
    result = polylist[0] #start py adding the first elem b/c it has no x multiplier
    for i in range(1,len(polylist)):
        result += polylist[i] * (x ** i)
        print(polylist[i], i, result)

    # for i in range(0,len(polylist)):
    #     result += polylist[i] * (x ** i)
    #     print polylist[i], i, result

    print(float(result))


poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
#print evaluate_poly(poly, -13)


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).
    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)
    x2 + 8x + 13 
    Derivative = 2x + 8 (note that any constant is eliminated, because essentially that was 13x^0,
     and when the 0 comes down the whole term becomes 0)
    3x2 + x + 9
    Derivative = 6x + 1
    4x4 + 3x3 + x + 19
    Derivative = 16x3 + 9x2 + 1
    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ...
    result = ()
    for i in range(0, len(poly)):
        if poly[i] != 0.0:
            #print "poly[i] = ", poly[i]
            #print "i - 1 = ", i
            #print "poly[i] * (i) = ", poly[i] * (i)
            result += (poly[i]*(i),)
        else:
            continue
    return result  
##i am not getting the same ans 
## (0.0, 35.0, 9.0, 4.0)
## i am getting "-" sign

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.
    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)
    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    #TO DO.....
    iteration = ()
    fguess = evaluate_poly(poly, x_0) #evaluates poly for first guess
    print(fguess)
    x_guess = x_0 #initialize x_guess
    if (fguess > 0 and fguess < epsilon): #if solution for first guess is close enough to root return first guess
        return x_guess
    else:
        while fguess > 0 and fguess > epsilon:
            iteration+=1
            x_guess = x_0 - (evaluate_poly(poly,x_0)/df(poly, x_0))
            fguess = evaluate_poly(poly, x_guess)
            if fguess > 0 and fguess < epsilon:
                break #fguess where guess is close enough to root, breaks while loop, skips else, return x_guess
            else:
                x_0 = x_guess #guess again with most recent guess as x_0 next time through while loop
    return x_guess

poly = (-13.39, 0.0, 17.5, 3.0, 1.0) 
x_0 = 0.1
epsilon = .0001
print(compute_root(poly, x_0, epsilon))


##  i am getting this error "not supported between instances of 'NoneType' and 'int'"