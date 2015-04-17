from nose.tools import eq_

import main

def test_for_3():
    number = 3
    eq_(main.count(number), 555)

def test_for_5():
    number = 5
    eq_(main.count(number), 33333)

def test_for_2():
    number = 2
    eq_(main.count(number), -1)

def test_for_7():
    number = 7
    eq_(main.count(number), -1)

def test_for_11():
    number = 11
    eq_(main.count(number), 55555533333)

def test_for_8():
    number = 8
    eq_(main.count(number), 55533333)

def test_for_30():
    number = 30
    eq_(main.count(number), int('555' * 10))

def test_for_115():
    number = 115
    eq_(main.count(number), 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333)
