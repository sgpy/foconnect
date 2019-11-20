# -*- coding: utf-8 -*-
"""
Demonstrating syntax for -
1- defining functions.
2- invoking them.

Python thrives on convention
for code formatting always refer to
https://www.python.org/dev/peps/pep-0008/
"""

def add(first, second):
    '''
    A simple function whicn takes in two arguments and adds them together,
    
    demonstrates how a simple python function should be defined.
    
    :param first: first argument.
    :param second: second argument.
    :return: the result of adding first and second.
    
    This whole text is a docstring, and in REPL environment, help() call on to
    this function name will result in this text getting displayed.
    '''
    return first + second


# same function can now be referred by another variable called 'sum'
# this is part of the message 
# "functions are first-class members of the language"
sum = add


def myOwnPrint(whatToPrint):
    """
    A function with side effects, which does not returns anything.
    
    :param whatToPrint: takes in what to print, and prints it.
    :param return: does not invoke the return statement, so Python's default
    behavior to return a "None" kicks in.
    """
    print(whatToPrint)
    
    
def addWithADefinitePrint(first, second):
    '''
    A simple function whicn takes in two arguments and adds them together,
    
    while doing so... also prints the result before returning, 
    so has a side effect.
    
    :param first: first argument.
    :param second: second argument.
    :return: the result of adding first and second.
    '''
    result = first + second
    print(result)
    return result


def addWithAPossibilityOfPrint(first, second, doPrint=False):
    '''
    A simple function whicn takes in two arguments and adds them together,
    
    also takes a third argument as a flag, which if set
    prints the result before returning, so this function 
    possibly has a side effect.
    
    :param first: first argument.
    :param second: second argument.
    :param doPrint (default False): if set to True, will print the result.
    :return: the result of adding first and second.
    '''
    result = first + second
    if doPrint:
        print(result)
    return result
