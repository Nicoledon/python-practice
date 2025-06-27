"""
HW 0: Finger Exercises

Instructions:
Fill out each method. You may assume inputs are well-formed.
Examples are given for each method. Do not use any external libraries 
except for defaultdict. The runtime of these functions does not need
to be optimal, implement them however you wish. Tests are not 
required but you may find it useful to manually test things yourself.

Submission:
Upload your filled-out finger_exercises.py to Canvas.
"""

from collections import defaultdict

# Let's start with some light warmups!

def filter_tuple_list(tuple_list, threshold):
    """
    Given a list of tuples where each tuple contains a string and a number,
    return a new list with only the tuples where the number is greater
    than the threshold.
    
    Example:
    >>> filter_tuple_list([('apple', 5), ('banana', 3), ('cherry', 7)], 4)
    [('apple', 5), ('cherry', 7)]
    """
    pass
    container = []
    for item in tuple_list:
        if item[1] >= threshold:
           container.append(item)
    return container
         


def count_items(nested_list):
    """
    Given a nested list of items, return a dictionary counting how many
    times each item appears. Items may be nested at any level.
    
    Example:
    >>> count_items([1, [2, 3], [2, [1, 4]]])
    {1: 2, 2: 2, 3: 1, 4: 1}
    """
    pass
    dic = {}
    count_items_helper(nested_list, dic)
    return dic
def count_items_helper(nested_list , dic):
    for item in nested_list:
        if isinstance(item,list):
            count_items_helper(item,dic)
        else :
            if item in dic:
                dic[item] += 1
            else :
                dic[item] = 1


def group_by_first_char(strings):
    """
    Given a list of strings, return a dictionary grouping strings by
    their first character. Ignore case (treat 'A' and 'a' as the same).
    
    Example:
    >>> group_by_first_char(['Apple', 'ant', 'Banana', 'bee'])
    {'a': ['Apple', 'ant'], 'b': ['Banana', 'bee']}
    """
    pass
    
def find_unique_values(dict_list):
    """
    Given a list of dictionaries, return a dictionary where each key
    is a key from the input dictionaries and each value is a set of
    unique values for that key across all dictionaries.
    
    Example:
    >>> find_unique_values([{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 2}])
    {'x': {1, 2}, 'y': {2, 3}}
    """
    pass


def all_substrings(s):
    """
    Return a set of all substrings of the given string s.

    Example:
    >>> all_substrings('abc')
    {'', 'a', 'b', 'c', 'ab', 'bc', 'abc'}

    EXTRA CREDIT: Do this in a single line of code.
    """
    pass


def tuplize(d):
    """
    Convert a dictionary into a list of tuples where each tuple is
    in the format (key, value).

    Example:
    tuplize({"a": 1, "b": "hello", "c": 3})
    [("a", 1), ("b", "hello"), ("c", 3)]

    EXTRA CREDIT: augment your function to handle nested dictionaries.
    Example:
    tuplize({"a": 1, "b": {"b2": 2, "b3": 3}, "c": 4})
    [("a", 1), ("b", [("b2", 2), ("b3", 3)]), ("c", 4)]
    """
    pass


# Now that your fingers are warm, let's do something a bit more involved :)

def sieve(n):
    """
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Implement the "Sieve of Eratosthenes" to find all primes less than 
    or equal to n. Return them as a sorted list.

    The algorithm in a nutshell:
    1.  Initialize a boolean list of size n+1 to True. This will keep
        track if each number is prime or not. We know that indices 0 and
        1 are False.
    2.  Starting with i=2, for entry i in the list, if it is True, 
        mark any value that is a multiple of i as False. Do this for
        all 2 <= i <= n.
    3.  Now, any index that has a mark of True is a prime. Return 
        these indices.

    Example:
    sieve(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    pass
    

def prime_decomposition(n):
    """
    Use the above sieve() function to implement prime decomposition. 
    That is, given n, return the list of primes that multiply to n.
    The list of prime divisors should be in sorted order.

    HINT: use modulo to determine if something divides n

    Example:
    prime_decomposition(50)
    [2, 5, 5]
    """
    pass
