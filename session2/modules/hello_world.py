#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file based python code HELLO WORLD...
"""


# Modules can also contain executable code, which can be used to 
# modify the import time behavior.

# So this will get executed, everytime this module is imported.
print('name of module is %s' %  __name__)


# This will get executed only when the name of the module is __name__
if __name__ == "__main__":
    print("Hello World!!!")

