"""
Test cases the halloween party in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    case1 = 12
    case2 = 6
    case3 = 10
    case4 = 20
    case5 = 3
    case6 = 2
    case7 = 11

    eq_(main.count(case1), 36)
    eq_(main.count(case2), 9)
    eq_(main.count(case3), 25)
    eq_(main.count(case4), 100)
    eq_(main.count(case5), 2)
    eq_(main.count(case6), 1)
    eq_(main.count(case7), 30)
