#!/usr/bin/python

from main import flipbits as main
from nose.tools import eq_

def test_flipbits_1():
    eq_(main(1), 4294967294)
def test_flipbits_2():
    eq_(main(0), 4294967295)
def test_flipbits_3():
    eq_(main(222341), 4294744954)
