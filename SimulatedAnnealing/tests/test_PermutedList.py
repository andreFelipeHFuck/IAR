import pytest

from utils.PermutedList import *

def test_repeated_element_exception():
    with pytest.raises(PermutedListRepeatedElementException):
        pl: PermutedList = PermutedList([1, 1])

def test_swap_index_exception():
    with pytest.raises(PermutedListSwapIndexException):
        pl: PermutedList = PermutedList([1, 2, 3])
        pl.swap_elems(4)

def test_list_elems():
    l: list[int] = [1, 2, 3]
    pl: PermutedList = PermutedList(l)
    assert l == pl.list_elems()
    
def test_list_pair_elems():
    l: list[int] = [1, 2, 3]
    exp: list[tuple(int, int)] = [(1, 2), (2, 3)]
    pl: PermutedList = PermutedList(l)
    
    assert pl.list_pair_elems() == exp
    
def test_swap_elems():
    l: list[int] = [1, 2, 3]
    
    exp_index_0: list[int] = [2, 1, 3]
    exp_index_1: list[int] = [1, 3, 2]
    exp_index_2: list[int] = [1, 3, 2]
    
    pl_0: PermutedList = PermutedList(l)
    pl_0.swap_elems(0)
    
    pl_1: PermutedList = PermutedList(l)
    pl_1.swap_elems(1)
    
    pl_2: PermutedList = PermutedList(l)
    pl_2.swap_elems(2)
    
    assert exp_index_0 == pl_0.list_elems()
    assert exp_index_1 == pl_1.list_elems()
    assert exp_index_2 == pl_2.list_elems()