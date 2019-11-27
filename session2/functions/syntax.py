# -*- coding: utf-8 -*-
"""
Demonstrating syntax for -
1- defining functions.
2- invoking them.

Python thrives on convention
for code formatting always refer to
https://www.python.org/dev/peps/pep-0008/
"""


# various ways for function definitions ###############################
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


def some_i_know_others_dont_know_how_many(first, second, *args):
    '''
    A function which demonstrates variable list of arguments.
    '''
    print("first - %s"  % str(first))
    print("second - %s"  % str(second))
    print("rest - %s"  % str(args))
    
    
def some_i_know_others_dont_know_what_all(first, second, *args, **kwargs):
    '''
    A function which demonstrates variable list of arguments.
    and the variable list of named arguments
    '''
    print("first - %s"  % str(first))
    print("second - %s"  % str(second))
    print("rest in the list - %s"  % str(args))
    print("rest in the dict - %s" % str(kwargs))
    
#########################################################
    
###############function invocation using unpacked collections###############
def sum(first, second, third, fourth=10):
    '''
    demo function to be used in 
    '''
    print("first - %s" % str(first))
    print("second - %s" % str(second))
    print("third - %s" % str(third))
    print("fourth - %s" % str(fourth))
    

def unpacking_list_for_arguments():
    lst = [10, 20, 30]
    sum(*lst)
    
    print("-"*10)
    
    lst.append(90)
    sum(*lst)


def unpacking_dict_for_arguments():
    dct = {'first': 10, 'third': 40, 'second': 30, 'fourth': 67}
    sum(**dct)
    print("-"*10)
    dct = {'third': 40,  'fourth': 67}
    sum(1, 2, **dct)
    
##############Globals and Locals##########################
iAmAGlobal = 200

def localOverride():
    '''
    simple function which overrides a global variable locally.
    '''
    print("will modify locally")
    iAmAGlobal = 4
    print("locally  it is - %d" % iAmAGlobal)


def globalModified():
    '''
    simple function which modifies a global variable, impacts everyone.
    '''
    print("will modify globally")
    global iAmAGlobal
    iAmAGlobal = 4
    print("locally  it is - %d" % iAmAGlobal)
#########################################################


####################Iteration Vs. Recursion###############
def fib_iter(n):
    '''
    fibonacci calculator, calculate the nth element in fib sequence.
    uses iteration.
    :param n: element no. in fib sequence.
    '''
    prev = 0
    element = 0   
    count = 0 
    next = 0
    while count <= n:        
        next = (element + prev) if count>1 else count
        prev = element
        element = next
        count = count + 1
    return next


def fibonacci(n):
    '''
    fibonacci calculator, calculate the nth element in fib sequence.
    uses recursion.
    :param n: element no. in fib sequence.
    '''
    if n <= 1:  
        return n
    return fibonacci(n-2) + fibonacci(n-1)
############################################################

########################Nested Function######################

multiplier = 5

def all_i_know_is_how_to_double(fn):
    '''
    nested function with a closure on a local variable.
    '''
    multiplier = 2
    def wrapped(*args, **kwargs):
        print("In my world multiplier is - %d" % multiplier)
        return multiplier*fn(*args, **kwargs)
    return wrapped


# once decorated - the decorator works upon the function to return another
# function. So the simple subtraction function gets modified to give
# double of the subtraction result.
@all_i_know_is_how_to_double
def difference(first, second):
    '''
    when this function was defined, it did a simple subtraction.        
    '''
    return first - second

multiplier = 10
##################################################################
    

if '__main__' == __name__:  
   print(multiplier)
   double_adder = all_i_know_is_how_to_double(add)
   print(add(10, 30))
   print(double_adder(10, 30))   
   
   print(difference(50, 10))
