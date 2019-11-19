#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple program to echo back what to say to it.
"""

# import random... we know "what it does", 
# do'nt care "How it does" as it is from credible source, 
# we rely on it.
import random


RANDOM_MESSAGES = [
        "wow....",
        "wait a minute brb...",
        "I think I have heard this before...",
        "OK..."
        ]


def random_choice( what_was_said ):
    return random.choice(RANDOM_MESSAGES)


def dumb_echo( what_was_said ):
    return what_was_said


def sheer_flattery(what_was_said):
    return("such beautiful words.... this is poetry")
    
    
def apprehensive(what_was_said):
    return("No way .. I dont trust you.")


# see the difference when the module is imported vs. when its executed.
print("%s is getting loaded." % __name__)

if __name__ == "__main__":
    words = input("Say something: ")
    print(dumb_echo(words))

    


