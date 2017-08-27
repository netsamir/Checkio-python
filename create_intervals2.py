#!/usr/bin/env python

fst = lambda ab: ab[0]
snd = lambda ab: ab[1]
head = lambda xs: xs[0]
tail = lambda xs: xs[1:]

def is_inter(a, b):
    """ Integer -> Integer -> Bool"""
    return  a == b - 1 or a == b

def list_sort(data):
    """ :: set -> [Integer],
    where the result is sorted
    """
    return sorted(list(data))

def interm(ab, n):
    """ :: (Integer, Integer) -> Integer -> (Integer, Integer) """
    if is_inter(snd(ab), n):
        return fst(ab), n
    else:
        return n, n

def acc_reduce(xs, ab):
    """ [Integer] -> (Integer, Integer) -> [(Integer, Integer)]"""
    if xs == []:
        return [ab]
    else:
        x = head(xs)
        base = interm(ab, x)
        if base == (x, x):
            return [ab] + acc_reduce(tail(xs), base)
        else:
            return acc_reduce(tail(xs), base)

def create_intervals(the_set):
    if len(the_set) == 0:
       return []
    xs = list_sort(the_set)
    return tail(acc_reduce(xs, (head(xs), head(xs))))

def test_create_intervals():
    data = {1, 2, 3, 4, 5, 7, 8, 12}
    ls_data = [1, 2, 3, 4, 5, 7, 8, 12]
    data2 = {1, 2, 3, 6, 7, 8, 4, 5}
    assert is_inter(2, 3) == True
    assert is_inter(3, 3) == True
    assert is_inter(3, 2) == False
    assert is_inter(3, 5) == False
    assert interm((1,1), 2) == (1,2)
    assert interm((1,2), 4) == (4,4)
    assert list_sort(data) == ls_data
    assert create_intervals(data) == [(1, 5), (7, 8), (12, 12)]
    assert create_intervals(data2) == [(1, 8)]
    assert create_intervals({}) == []
    assert create_intervals({1}) == [(1, 1)]
    assert create_intervals({1, 1}) == [(1, 1)]
    assert create_intervals({1, 2, 3}) == [(1, 3)]
    assert create_intervals([]) == []

if __name__ == '__main__':
    test_create_intervals()
