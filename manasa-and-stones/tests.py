"""
Test cases the manasa and stones in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    case1 = [4, 10, 100]
    case2 = [6, 2, 2]
    case3 = [10, 5, 6]
    case4 = [20, 1, 2]
    case5 = [1, 10, 1]
    case6 = [2, 2, 2]
    case7 = [10, 2, 5]

    eq_(main.count(case1[0], case1[1], case1[2]), [30, 120, 210, 300])
    eq_(main.count(case2[0], case2[1], case2[2]), [10])
    eq_(main.count(case3[0], case3[1], case3[2]), [45, 46, 47, 48, 49, 50, 51, 52, 53, 54])
    eq_(main.count(case4[0], case4[1], case4[2]), [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38])
    eq_(main.count(case5[0], case5[1], case5[2]), [0])
    eq_(main.count(case6[0], case6[1], case6[2]), [2])
    eq_(main.count(case7[0], case7[1], case7[2]), [18, 21, 24, 27, 30, 33, 36, 39, 42, 45])
