"""
Given a list of integers l, return the list with each value multiplied by integer n.
Restrictions:

The code must not:

    contain *.
    use eval() or exec()
    contain for
    modify l

Happy coding :)
"""
import math


def multiply(n, l):
    result = list(map(lambda x: x.__mul__(n), l))
    return result
