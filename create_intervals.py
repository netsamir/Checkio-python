#!/usr/bin/env python

from itertools import tee, takewhile, dropwhile

fst = lambda x: x[0]
snd = lambda x: x[1]
last = lambda x: x[-1]

def toggle_tuple(the_list):
    """ :: [a] -> [(a, a)] """
    if len(the_list) == 1:
        return [(the_list[0], the_list[0])]
    return list(zip(the_list, the_list[1:]))

def untoggle_tuple(tuple_list):
    """ :: [(a, a)] -> [a] """
    if len(tuple_list) == 1:
        return [fst(fst(tuple_list))]
    return [fst(x) for x in tuple_list] + [snd(tuple_list[-1])]

def same_plus_1(nxt):
    """ :: [(Int, Int)] -> Bool"""
    return fst(nxt) == snd(nxt) - 1

def takewhile2(predicate, the_list):
    """ :: (a -> Bool) -> [a] -> ([a]', [a]'')
    where predicate([a]' ) == True
          [a]'' is the remaining
    """
    list_p, remaining = tee(the_list, 2)
    return list(takewhile(predicate, list_p)), list(dropwhile(predicate, remaining))

def convert(the_set):
    """ :: {Int} -> [Int],
    where value are ordered"""
    return sorted(list(the_set))

def group_end(seq):
    """ :: [(Int, Int)] -> (Int, Int),
    where value in result does not contain gap"""
    return fst(fst(seq)), snd(last(seq))

def process(list_):
    seq, remaining = takewhile2(same_plus_1, toggle_tuple(list_))
    if len(seq) == 1 and remaining == []:
        return tuple(seq), []
    return untoggle_tuple(seq), untoggle_tuple(remaining)[1:]

def create_intervals(the_set):
    return [ interval for interval in process(convert(the_set))]

def test_create_intervals():
    assert convert({0, 1, 2, 3, 4, 5 }) == list(range(6)), 'The list is not ordered'
    assert toggle_tuple([]) == []
    assert toggle_tuple([4]) == [(4,4)]
    assert toggle_tuple([1, 2, 3, 4]) == [(1,2), (2,3), (3,4)]
    assert untoggle_tuple([(1,2), (2,3), (3,4)]) == [1, 2, 3, 4]
    assert untoggle_tuple([(1,1)]) == [1]
    assert toggle_tuple([1, 2, 3, 4]) == toggle_tuple(untoggle_tuple([(1,2), (2,3), (3,4)]))
    assert same_plus_1((1, 2)) == True
    assert same_plus_1((1, 3)) == False
    assert takewhile2(lambda x: x <= 2, [1, 2, 3, 5]) == ([1, 2], [3, 5])
    assert takewhile2(same_plus_1, [(1, 2), (2, 3), (3, 5)]) == ([(1, 2), (2, 3)], [(3, 5)])
    assert takewhile2(same_plus_1, [(1, 1)]) == ([], [(1,1)])
    assert takewhile2(same_plus_1, [(1, 2)]) == ([(1, 2)], [])
    assert process([1, 2, 3, 4, 5, 7, 8, 12]) == ([1, 2, 3, 4, 5], [7, 8, 12])
    assert process([1, 2, 3, 4]) == ([1, 2, 3, 4], [])
    assert process([1, 2]) == ([1, 2], [])
    assert group_end([(1, 2), (2, 3), (5, 9), (10, 12)]) == (1,12)
#    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == None


if __name__ == '__main__':
    test_create_intervals()
