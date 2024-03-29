"""
The prime 149 has 3 permutations which are also primes: 419, 491 and 941.

There are 3 primes below 1000 with three prime permutations:

149 ==> 419 ==> 491 ==> 941
179 ==> 197 ==> 719 ==> 971
379 ==> 397 ==> 739 ==> 937

But there are 9 primes below 1000 with two prime permutations:

113 ==> 131 ==> 311
137 ==> 173 ==> 317
157 ==> 571 ==> 751
163 ==> 613 ==> 631
167 ==> 617 ==> 761
199 ==> 919 ==> 991
337 ==> 373 ==> 733
359 ==> 593 ==> 953
389 ==> 839 ==> 983

Finally, we can find 34 primes below 1000 with only one prime permutation:

[13, 17, 37, 79, 107, 127, 139, 181, 191, 239, 241, 251, 277, 281, 283, 313, 347, 349, 367, 457, 461, 463, 467, 479,
563, 569, 577, 587, 619, 683, 709, 769, 787, 797]

Each set of permuted primes are represented by its smallest value, for example the set 149, 419, 491, 941 is represented
by 149, and the set has 3 permutations.

Notes

    the original number (149 in the above example) is not counted as a permutation;
    permutations with leading zeros are not valid

Your Task

Your task is to create a function that takes two arguments:

    an upper limit (n_max) and
    the number of prime permutations (k_perms) that the primes should generate below n_max

The function should return the following three values as a list:

    the number of permutational primes below the given limit,
    the smallest prime such prime,
    and the largest such prime

If no eligible primes were found below the limit, the output should be [0, 0, 0]
Examples

Let's see how it would be with the previous cases:

permutational_primes(1000, 3) ==> [3, 149, 379]
''' 3 primes with 3 permutations below 1000, smallest: 149, largest: 379 '''

permutational_primes(1000, 2) ==> [9, 113, 389]
''' 9 primes with 2 permutations below 1000, smallest: 113, largest: 389 '''

permutational_primes(1000, 1) ==> [34, 13, 797]
''' 34 primes with 1 permutation below 1000, smallest: 13, largest: 797 '''

Happy coding!!

"""


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def permutational_primes(n_max, k_perms):
    prime_numbers = {}
    result_numbers = {}
    min_number, max_number, counter = n_max, 0, 0
    for number in range(n_max):
        if is_prime(number):
            sorted_number = "".join(sorted(str(number)))
            if sorted_number not in prime_numbers:
                prime_numbers[sorted_number] = number
                result_numbers[number] = set()
            else:
                result_numbers[prime_numbers[sorted_number]].add(number)
    for number in result_numbers:
        if len(result_numbers[number]) == k_perms:
            min_number = min(min_number, number)
            max_number = max(max_number, number)
            counter += 1
    return [counter, min_number, max_number] if counter else [0, 0, 0]
