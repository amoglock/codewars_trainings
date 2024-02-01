"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its
digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""


def next_bigger(n):
    list_digits = list(str(n))
    i = len(list_digits) - 2
    while i >= 0 and list_digits[i] >= list_digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = len(list_digits) - 1
    while list_digits[j] <= list_digits[i]:
        j -= 1

    list_digits[i], list_digits[j] = list_digits[j], list_digits[i]
    list_digits[i + 1:] = reversed(list_digits[i + 1:])
    return int(''.join(list_digits))
