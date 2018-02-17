""" recursion exercises with nested lists
"""
from typing import List, Union


def gather_lists(list_: List[List[object]]) -> List[object]:
    """
    Return the concatenation of the sublists of list_.

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def list_all(obj: Union[list, object]) -> list:
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = ['ji', 2, 3, 4]
    >>> list_all(obj)
    ['ji', 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    if not isinstance(obj, list):
        return [obj]
    else:
        return gather_lists([list_all(x) for x in obj])


def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length(['ji', 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    >>> max_length([[1, 2, [3, 4 ,5 ,6 ,7 ,8], 3], 4, [4, 5]])
    6
    """
    if not isinstance(obj, list):
        return 0
    elif all([not isinstance(i, list) for i in obj]):
        return len(obj)
    else:
        return max(max_length(x) for x in obj)


def list_over(obj: Union[list, str], n: int) -> List[object]:
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    if not isinstance(obj, list) and len(obj) > n:
        return [obj]
    elif not isinstance(obj, list) and len(obj) <= n:
        return []
    else:
        return gather_lists([list_over(x, n) for x in obj])


def list_even(obj: Union[list, int]) -> List[object]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    if not isinstance(obj, list) and obj % 2 == 0:
        return [obj]
    elif not isinstance(obj, list) and not (obj % 2 == 0):
        return []
    else:
        return gather_lists([list_even(x) for x in obj])


def count_even(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    if not isinstance(obj, list) and obj % 2 == 0:
        return 1
    elif not isinstance(obj, list) and not (obj % 2 == 0):
        return 0
    else:
        return sum([count_even(x) for x in obj])


def count_odd(obj: Union[list, int]) -> int:
    """
    Return the number of odd numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an odd number and 0 if it is an even number.

    >>> count_odd(3)
    1
    >>> count_odd(16)
    0
    >>> count_odd([1, 2, [3, 4], 5])
    3
    """
    if not isinstance(obj, list) and not (obj % 2 == 0):
        return 1
    elif not isinstance(obj, list) and (obj % 2 == 0):
        return 0
    else:
        return sum([count_odd(x) for x in obj])


def count_all(obj: Union[list, object]) -> int:
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    if not isinstance(obj, list):
        return 1
    else:
        return sum([count_all(x) for x in obj])


def count_above(obj: Union[list, int], n: int) -> int:
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    if not isinstance(obj, list):
        return 1 if obj > n else 0
    else:
        return sum([count_above(x, n) for x in obj])
