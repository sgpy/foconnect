#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reaping what we sowed....
i.e. utilizing the functionality in the echo module.
"""

# import our echo module
import echo


if __name__ == "__main__":
    what_user_wants = input("%s %s %s %s" %
                    ("what do you want Apprehension(A) or",
                     "Flattery(F) or",
                     "Random(R) or",
                     "Honest Dumbness(D) ?"))
    action = None
    if what_user_wants == 'A':
        action = echo.apprehensive
    elif what_user_wants == 'F':
        action = echo.sheer_flattery
    elif what_user_wants == 'R':
        action = echo.random_choice
    elif what_user_wants == 'D':
        action = echo.dumb_echo
    else:
        print("do not understand what you want....")
    
    if action:
        words = input("Say something....:")
        print(action(words))

        
    

