#!/usr/bin/env python
from itertools import count, repeat, cycle, islice, tee, repeat, accumulate, chain

head = next

def tail(it):
    next(it)
    return it

def take(n, it):
    return [x for x in islice(it, n)]

def drop(n, it):
    return islice(it, n, None)

def iterate(f, x):
    """return (x, f(x), f(f(x)), ...)"""
    return accumulate(repeat(x), lambda fx, _: f(fx))

def list_sort(data):
    return sorted(list(data))

def accumulate_until(ls_data, func):
    """ :: [Integer] -> (Int -> Bool) -> (Int, Int) """

is_inter = lambda x, y: x == y - 1 or x == y

def create_intervals(the_set):
   ls_data = list_sort(the_set) 
   
def test_create_intervals():
    data = {1, 2, 3, 4, 5, 7, 8, 12}
    ls_data = [1, 2, 3, 4, 5, 7, 8, 12]
    data2 = {1, 2, 3, 6, 7, 8, 4, 5}
    assert is_inter(2, 3) == True
    assert is_inter(3, 3) == True
    assert is_inter(3, 2) == False
    assert is_inter(3, 5) == False
    assert list_sort(ls_data, is_inter) == ls_data
    assert accumulate_until(ls_data) == (1,5)
    assert create_intervals(data) == [(1, 5), (7, 8), (12, 12)]
    assert create_intervals(data2) == [(1, 8)]

if __name__ == '__main__':
    test_create_intervals()
