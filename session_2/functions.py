def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    # Below can be rewritten with ternary operator
    # return num if num >= 0 else -num
    if num >= 0:
        return num
    else:
        return -num


# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))
