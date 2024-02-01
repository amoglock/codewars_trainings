"""
This kata is based on a variation of Happy Numbers by TySlothrop. It is advisable to complete it first to grasp the idea
and then move on to this one.

Hello, my dear friend, and welcome to another Happy Numbers kata! What? You're not interested in them anymore? They are
all the same? But what if I say that this one is a performance version...
Your task:

Write a function which takes a number n as an argument and returns a list of all "happy numbers" from 1 to n inclusive.
For example:

10   =>  [1, 7, 10]
50   =>  [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
100  =>  [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]

Test suite:

    5000 tests with number n being up to 300_000
    you are not allowed to hardcode the sequence - you must compute it (max length of the code is 1700 characters)
"""


def performant_numbers(n):
    list_happy_numbers = []
    for i in range(1, n + 1):
        number = i
        checked_numbers = set()
        while number > 1 and number not in checked_numbers:
            checked_numbers.add(number)
            number = sum(x * x for x in map(int, str(number)))

        if number == 1:
            list_happy_numbers.append(i)
    return list_happy_numbers


print(performant_numbers(10))
