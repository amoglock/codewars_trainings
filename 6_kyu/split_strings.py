"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of
characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
import re


def solution(s):
    if len(s) % 2:
        s += "_"
    return [s[a:a+2] for a in range(0, len(s), 2)]

    # A cool one-line solution using the re module.
    # Using re.findall("..", s + "_") we split the string into pairs of characters.
    # ".." - means that we find any two symbols. The dot symbol match with any symbol exclude the new line symbol.
    # s + "_" - means that we add underscore symbol to end of line always. If len the line is odd the symbol makes it
    # even. Otherwise, the symbol omit (because the last character is single).

    # return re.findall("..", s + "_")
