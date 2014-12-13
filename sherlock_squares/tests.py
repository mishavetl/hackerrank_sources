"""
Test cases for sherlock and squares in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    numbers1 = [6, 15]
    numbers2 = [7, 17]
    numbers3 = [0, 16]
    numbers4 = [7, 100]
    numbers5 = [30, 80] #[1000000, 4000000]
    numbers6 = [1, 5]

    eq_(main.find_squares(numbers1), 1)
    eq_(main.find_squares(numbers2), 2)
    eq_(main.find_squares(numbers3), 4)
    eq_(main.find_squares(numbers4), 8)
    eq_(main.find_squares(numbers5), 3)
    eq_(main.find_squares(numbers6), 2)
