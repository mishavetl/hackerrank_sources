"""
Test cases for Game Of Trones - 1 in hackerrank

author: mishavietl

"""

from nose.tools import eq_
from main import count


def test_count():
    case1 = "aabbabb"
    case2 = "ccaabb"
    case3 = "jllkd"
    case4 = "nbmmbn"

    eq_(count(case1), "YES")
    eq_(count(case2), "YES")
    eq_(count(case3), "NO")
    eq_(count(case4), "YES")
