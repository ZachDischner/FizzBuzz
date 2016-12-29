#! /usr/local/bin/python

"""Zach Dischner's submission to the modified fizz-buzz programming challenge
listed at https://github.com/swift-nav/screening_questions/blob/master/questions.md#swift-navigation-application-questions

"""

##############################################################################
#                                   Imports
#----------*----------*----------*----------*----------*----------*----------*
from  __future__ import print_function   # Should really be using Python 3.5+
import sys
import argparse
import numpy as np


##############################################################################
#                                  Functions
#----------*----------*----------*----------*----------*----------*----------*
def is_prime(x):
    """Determine if a number is prime or not
    
    Algo:
        Less than 2 is not prime
        2 is prime
        Evens greator than 2 are not prime
        Otherwise check to see if any number up to sqrt(x) goes into x evenly

    Args:
        x:  (integer) number to test for primeness

    Returns:
        _   (bool) Boolean indicator of primeness 

    Examples:
        >>> is_prime(-1)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(6)
        False
        >>> is_prime(9)
        False
        >>> is_prime(49)
        False
    """
    assert type(x) is int, "is_prime requires integer type, provided {}".format(type(x))

    if x < 2:
        return False
    if x == 2:
        return True
    if (x % 2)==0:
        return False

    ## Check all odd number possible factors in range 3 - square root of x (nearest integer > )
    for possibility in range(3,int(x**0.5+1),2):
        if (x % possibility)==0:
            return False

    ## No more combos! Prime number here baby
    return True



def fib():
    """Memory efficient Fibonacci sequence generator
    """
    one_ago, two_ago = 0,1
    while True:
        yield one_ago
        one_ago, two_ago = two_ago, one_ago + two_ago

def fizz_buzzify(x):
    """Determined modified fizz-buzz representation of number `x`

    Rules:
        * if x is prime ==> "BuzzFizz"
        * if x is divisible by 15 ==> "FizzBuzz"
        * if x is divisible by 3 ==> "Fizz"
        * if x is divisible by 5 ==> "Buzz"
        * x ==> x otherwise
    
    Note the order of precidence. 3 is prime as well as divisible by 3. But we return 
    prime representation first. Logic follows that if prime didn't take precidence, then
    x%15 wouldn't take precidence either and then we'd be stuck without ever having that
    occurance and trying to figure out if "Fizz" or "Buzz" is the correct implementation. 

    Examples:
    >>> fizz_buzzify(10)
    'Buzz'
    >>> fizz_buzzify(11)
    'BuzzFizz'
    >>> fizz_buzzify(12)
    'Fizz'
    >>> fizz_buzzify(15)
    'FizzBuzz'
    >>> fizz_buzzify(16)
    16
    """
    ## First test for primeness
    if is_prime(x):
        return "BuzzFizz"
    
    ## Now check the rest 
    divis_3 = ""
    divis_5 = ""
    if (x % 3) == 0:
        divis_3 += "Fizz"
    if (x % 5) == 0:
        divis_5 += "Buzz"

    ## Assemble fizzbuzzed string or return the number. handy one liner
    return (divis_3 + divis_5) or x


def generate_fizz_buzz(N):
    """Generates a fizz-buzzed Fibonacci Sequence of length N
    """
    for index, fib_number in enumerate(fib()):
        if index > N:
            break
        print(fizz_buzzify(fib_number))



##############################################################################
#                                  Tests
#----------*----------*----------*----------*----------*----------*----------*
def test_fib():
    fibgen = fib()
    fib5 = [next(fibgen) for ix in range(5)]
    truth = [0,1,1,2,3]
    assert fib5==truth, "Fibonacci sequence generator failed, {} should == {} but it doesnt".format(fib5,truth)

##############################################################################
#                                  Runtime
#----------*----------*----------*----------*----------*----------*----------*
if __name__ == "__main__":
    ###### Gather arguments
    parser   = argparse.ArgumentParser(description='Fizz-Buzzify a Fibonacci sequence',
                    epilog='Example of use: python fizzbuzz.py 5')
    parser.add_argument('N', type=int, help="Length of Fibonacci Sequence to produce")
    args = parser.parse_args()
    N = args.N

    ###### Generate Fizz Buzz'd Fibonacci Sequence
    print("Generating a Fibonacci sequence of length {N} for fizz-buzzifying".format(N=N))
    generate_fizz_buzz(N)
    sys.exit(0)


