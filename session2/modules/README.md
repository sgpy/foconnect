# Modules in Python

###### reference documentation - 
- https://docs.python.org/3.7/tutorial/modules.html
- https://en.wikipedia.org/wiki/Modular_programming
- https://www.python.org/dev/peps/pep-0008/
 

Assuming you are aware of how to play around with Python interpreter.
REPL - Read-Eval-Print Loop - good for quick checks and experiments.
Also good for quckly handling support queries. Not scalable for development
of even moderate complexity.

#### Modularity
- provides cognitive simplification (divide and conquer), which in turn allows for scalability i.e. ability to add more and more features to a single system.
- provides reliability - aggregate of individually reliable small constituents
    compared to a monolithic system.
- improves reusability - small well defined independent modules can be assembled    in different configuration for different uses.
- Allows for division of labour for faster development across bigger teams.
- as an extension allows for use of third party modules and thus efficiency.

- Modularity as a concept spans across different aspects of python programming.
   - logical separation of a code in "Packages" - manifested as folders.
   - Python "modules" (obviously) - manifested as files
   - Then you can have your logic level modularity in the form of "functions".
   - self contained "class definitions" are yet another layer of modularity.
    
- Modularity can be hierarchical -
    - packages
        - sub-pacakges
            - files( a.k.a Python modules)
                - definitions in a Python module

##### Packages
think of them as folder structures which separate out your files.
   - they allow for sub packages - so a tree like structure - additional hierarchy.
   - help in separating two files with same name.
   - presence of "\_\_init\_\_.py" allows python to distinguish a python package from a regular file folder. Can be empty or can have '\_\_all\_\_' variable.
   - files/modules with same name can be in different packages - just like files.


##### Modules
These are actual code files organized across package structures. The python code specified in these modules defines further modular constructs like function definitions, class definitions etc.
- definitions in a module can be imported by other modules
    - selectively some of them (from abc import x, y, z)
    - or all of the definitions in one shot (import abc) or (from abc import *).
- definitions consist of variable definitions, function definitions, user defined class definitions.
  file level hierarchy is referred as "module" (file sans '.py' is module name)
  "\_\_name\_\_" at runtime resolves to the name of the module.

- Modules can also contain executable code, which can be used to modify the import time behavior. This behavior can be exploited to make a module execute too. Python interpretter when it is given a module path to execute, it loads it and gives it a unique name "\_\_main\_\_".
