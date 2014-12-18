"""
Test cases the filling jars in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    case1 = [1, 2, 100, 0]
    case2 = [3, 5, 6, 0]
    case3 = [1, 10, 6, 0]
    case4 = [3, 6, 60, 0]
    case5 = [1, 2, 145, 0]
    case6 = [1, 2, 2, 0]
    case7 = [4, 6, 5, 0]

    eq_(main.count(case1[0], case1[1], case1[2], case1[3]), 200)
    eq_(main.count(case2[0], case2[1], case2[2], case2[3]), 18)
    eq_(main.count(case3[0], case3[1], case3[2], case3[3]), 60)
    eq_(main.count(case4[0], case4[1], case4[2], case4[3]), 240)
    eq_(main.count(case5[0], case5[1], case5[2], case5[3]), 290)
    eq_(main.count(case6[0], case6[1], case6[2], case6[3]), 4)
    eq_(main.count(case7[0], case7[1], case7[2], case7[3]), 15)
