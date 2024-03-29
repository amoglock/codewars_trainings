"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that
character appears only once in the original string, or ")" if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the
"XXX" is the expected result, not the input!

"""
from collections import defaultdict


def duplicate_encode(word):
    result = defaultdict(int)
    for character in word.lower():
        result[character] += 1
    return "".join(["(" if result[c] == 1 else ")" for c in word.lower()])
