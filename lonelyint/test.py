#!/usr/bin/python

from main import lonelyinteger as main
from nose.tools import eq_

def test_lonelyint_big_list_one_appears_1():
    eq_(main([1, 1, 1, 3, 2, 2, 3, 4]), 4)
def test_lonelyint_big_list_three_appears_2():
    eq_(main([1, 6, 3, 2, 2, 3, 4, 5]), 1)
def test_lonelyint_normal_list_one_appears_3():
    eq_(main([3, 3, 3, 3, 1]), 1)
def test_lonelyint_normal_list_five_appears_4():
    eq_(main([1, 2, 3, 4, 5]), 1)
def test_lonelyint_small_list_one_appears_5():
    eq_(main([1, 1, 7]), 7)
def test_lonelyint_small_list_two_appears_6():
    eq_(main([3, 3, 1, 2]), 1)
