"""
Test cases for find_digits in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    number1 = 15
    number2 = 0
    number3 = 45
    number4 = 1023
    number5 = 55
    number6 = 11660

    eq_(main.main(number1), 2)
    eq_(main.main(number2), 0)
    eq_(main.main(number3), 1)
    eq_(main.main(number4), 2)
    eq_(main.main(number5), 2)
    eq_(main.main(number6), 2)
