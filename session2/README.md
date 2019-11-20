# Session 2

##### Theme - Modularity - I
- ###### Python Packages
- ###### Python Modules
- ###### Python Functions

##### Session Exercise 
- ###### Problem Statement
    - read fx rates from a CSV file
    - read Local Currency positions for different books from an Excel sheet
    - Generate CSV file with USD positions for those books.
- ###### Session Exercise Goal
    - break down a given problem statement.
    - plan modular components - packages, modules and functions for a given problem.
    - decide what third party components to use.
    - implement.


##### Offline Exercise problems
###### 1 - Pure function which converts 2D cartesian coordinates into polar co-ordinates:
(x, y) => (r, theta)
here r is positive square root of sum of squares of x and y
and theta is inverse tan (arctan) of ratio of y over x 
you can refer to https://docs.python.org/3.7/library/math.html#module-math
for math functions. 

###### 2 - Single variable numerical integration:
given a single variable mathematical function y = f(x), given boundary conditions for x [x1, x2]
area under the curve y=f(x) is the integral of this function between those boundary values of x. 
Numerically (using a computer) this can be done by dividing that area into thin rectangular slices 
(thickness of each slice is called a 'dx') and then summing up the area of those slices to get a 
good approximation of total area. Thinner the slices, slower your calculation but better the approximation of total area.

write a python function which takes in -
- an arbitrary single valye mathematical function say 
math.sin(x) or math.exp(x) or math.sin(x)^2 + math.cos(x)^2 etc.
(you can ‘import math’ to get math functions in your code.)
- boundary conditions x1 and x2 for x    say x1 = 0 and x2 = 2*math.pi  
(yes you can ‘import math’ to let python tell you the value of pi.)
- thickness of the rectangular slices (so called 'dx') say dx = 0.000001
 
and then calculates the integral.


- Pallindrome detector.
