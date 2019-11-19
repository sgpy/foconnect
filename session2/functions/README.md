# Functions in python

###### reference documentation - 
    - https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions
    - https://en.wikipedia.org/wiki/Modular_programming
    - http://www.trytoprogram.com/python-programming/python-closures/
    - https://en.wikipedia.org/wiki/Functional_programming


- think of cooking, think of recipes that take some ingredients and then 
    - do something or 
    - create something new.
    
- when working on one recipe, you can invoke another recipe to cook a sub ingredient.
- definition of a function is different from invocation of a function.
- carries all the benefits of "Modularity"
    - simplification so scalability (divide and conquer).
    - reliability
    - reusability
    - ease for development across big teams.
    - huge number of third party defined functions available.
- There are arguments to a function and returns coming out of a function. Some functions dont return anything.
 
##### Global and local variables
- variables defined within a function are meant for use within the function only.
- variables defined outside of the function in the same or higher scope as the function read only visibility inside the function, but if it needs to be modified the "global" keyword is needed.
 
##### Recursive function definitions
- a function which calls onto itself. 
- definition becomes concise, but may not be good from computational performance point of view.
- recursion and iteration equivalence.

##### Nested function definitions
- most of the time you will find that you have function definitions which are only invoking other functions defined outside.
- in some unique situations you may need to define a new function inside another function definition
- Nested functions have "closure" of state at the time of thier definition.

##### Pure functions and then those with "Side Effects"
-  Pure Functions - functions which take in some arguments and without changing the arguments, build and return something new, and this behavior is consistent over time i.e. same results for same inputs whenever they are invoked.
-  Functions with Side Effects
    - those which change the incoming arguments.
    - those which change the state of the world.
    - none of the above two conditions, but inconsistent i.e. different results when invoked with same arguments at different times.
- Generally functions which do not return anything, are likely to have side effects.

|Benefits|Pure Functions|Functions with side effects|
|--------|--------------|---------------------|
|Reliability|high - as totally predictable (results in simple clear code)|may not be as high as some side effects not known at the time of development (can be low on code clarity)|
|Performance|Can be low on performance as replication but good for parallelization|Can be high as can use pre defined states but not suitable for parallelization|
|I/O behavior| not possible as they dont know how to interact with the world| all I/O functions are functions with side effect|
|Mathematical basis|formal mathematical model (Lambda Calculus)|imperative definitions so complex formal descriptions|

##### Functions as first class members of the language.
as good as any other data variables, function definitions can be assigned to variables, passed in as arguments to other functions and so on. This results in very expressive concise code. 

##### Syntax
- "def" keyword to define a function.
- the name and the arguments.
- like other block statements, use of ":" to define the body block
- Optional "return" statement to return results out of the function.
- Variety of ways to define arguments
   - simple arguments (all required).
   - some or all with "default" values, (default values set in stone at the time of definition).
   - Thumbrule - most uncertain ones to be on the left.
   - arbitrary arguments list.
   - arbitrary arguments as name-value pairs.
- Variety of ways to invoke functions
    - simple invocation specifying all the arg values. (Positional args)
    - relying on default values. (Positional args) 
    - invoking with named arguments. (Keyword args)
    - combination of Positional and keyword args
    - unpacking argument lists
    - unpacking name-value pair arguments.
- functions which return functions - with possibility of nested functions and functions being first class members, you can have functions which based on input arguments can return other functions. This can help in creating decorators.
