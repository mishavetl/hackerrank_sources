"""
Test cases the chocolate feast in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    case1 = [12, 4, 4]
    case2 = [6, 2, 2]
    case3 = [10, 5, 6]
    case4 = [20, 1, 2]
    case5 = [1, 10, 1]
    case6 = [2, 2, 2]
    case7 = [10, 2, 5]

    eq_(main.count(case1[0], case1[1], case1[2]), 3)
    eq_(main.count(case2[0], case2[1], case2[2]), 5)
    eq_(main.count(case3[0], case3[1], case3[2]), 2)
    eq_(main.count(case4[0], case4[1], case4[2]), 39)
    eq_(main.count(case5[0], case5[1], case5[2]), 0)
    eq_(main.count(case6[0], case6[1], case6[2]), 1)
    eq_(main.count(case7[0], case7[1], case7[2]), 6)
