"""
What is a happy number?

A happy number is defined as an integer in which the following sequence ends with the number 1.

    Calculate the sum of the square of each individual digit.

    If the sum is equal to 1, then the number is happy.

    If the sum is not equal to 1, then repeat from steps 1.

    A number is considered unhappy once the same number occurs multiple times in a sequence because this means there is
    a loop and it will never reach 1.

For example, the number 7 is a "happy" number:

7² = 49 --> 4² + 9² = 97 --> 9² + 7² = 130 --> 1² + 3² + 0² = 10 --> 1² + 0² = 1

On the other hand, the number 6 is not a happy number as the sequence that is generated is the following:

6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58, 89

Once the same number occurs twice in the sequence, the sequence is guaranteed to go on infinitely, never hitting the
number 1, since it repeat this cycle.

Your task:

Write a function perf_happy(n) that returns a list of all happy numbers from 1 to n inclusive.

perf_happy(100)   =>  [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]

The challenge:

    you are going to be challenged for 30 tests up to n = 10_000_000
    you are not allowed to hardcode the sequence: you'll have to compute it (max length of the code: 1700 characters)

Credits

This kata is based on a variation of Happy Numbers by TySlothrop.

It's a different view of Happy Numbers (performance edition) by FArekkusu.

(ok, ok, I've copied a lot from them)
"""


# def perf_happy(n):
#     result = [1]
#     for i in range(1, n + 1):
#         control_numbers = [i]
#         number = i
#         while True:
#             split_number = [int(digit) for digit in str(number)]
#             sum_squares = sum(x ** 2 for x in split_number)
#
#             if sum_squares == 1:
#                 result.append(control_numbers[0])
#                 break
#             if sum_squares in control_numbers:
#                 break
#             else:
#                 control_numbers.append(sum_squares)
#                 number = sum_squares
#     return result
    # for i in range(1, n + 1):
    #     split_number = list(str(i))
    #     sum_squares = sum(int(x) ** 2 for x in split_number)
    #     if sum_squares in control_numbers:
    #         continue
    #     if sum_squares == 1:
    #         control_numbers = []
    #         result.append(i)
    #     else:
    #         control_numbers.append(sum_squares)
    #         perf_happy(sum_squares)
    # return result


# def perf_happy(n):
#
#     happy_numbers = []
#     bad_numbers = set()
#     good_numbers = set()
#     for i in range(1, n + 1):
#         visited_numbers = set()
#         number = i
#
#         while number != 1:
#             if number in visited_numbers or number in bad_numbers:
#                 bad_numbers = bad_numbers.union(visited_numbers)
#                 break
#             if number in good_numbers:
#                 good_numbers = good_numbers.union(visited_numbers)
#                 happy_numbers.append(i)
#                 break
#             visited_numbers.add(number)
#             split_number = (int(digit) for digit in str(number))
#             number = sum(x * x for x in split_number)
#
#         if number == 1:
#             good_numbers = good_numbers.union(visited_numbers)
#             happy_numbers.append(i)
#     print(
#         bad_numbers
#     )
#     return happy_numbers
#
#
# print(perf_happy(200))