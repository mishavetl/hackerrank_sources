"""
Test cases the lovely letter mystery in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main

def test_main():
    """test for main function"""
    case1 = "aba"
    case2 = "abcd"
    case3 = "mike"
    case4 = "download"
    case5 = "jklmn"
    case6 = "death"
    case7 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case8 = "sajdjkdsjcnufhsjdhkncnnsudejnfdmkjkjadfhasfjhdsfkjhsjfheuruyuehbfd"
    case9 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasuuuuuuuuuudududududuudd"
    case10 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhaggggggg"
    case11 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case12 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case13 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case14 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case15 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case16 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case17 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case18 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case19 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case20 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case21 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case22 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case23 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"
    case24 = "mijasflksdjfasidfjklzzhzlhzlkjhdjkaslhfuiehrjklsdbfnkdjsvndksjanhdjfahkkkeuhyufgninxmsadhhjhasdfuer"

    eq_(main.polindrom(case1), 0)
    eq_(main.polindrom(case2), 4)
    eq_(main.polindrom(case3), 10)
    eq_(main.polindrom(case4), 24)
    eq_(main.polindrom(case5), 6)
    eq_(main.polindrom(case6), 19)
    eq_(main.polindrom(case7), 323)
    eq_(main.polindrom(case8), 201)
    eq_(main.polindrom(case9), 475)
    eq_(main.polindrom(case10), 315)
    eq_(main.polindrom(case11), 323)
    eq_(main.polindrom(case12), 323)
    eq_(main.polindrom(case13), 323)
    eq_(main.polindrom(case14), 323)
    eq_(main.polindrom(case15), 323)
    eq_(main.polindrom(case16), 323)
    eq_(main.polindrom(case17), 323)
    eq_(main.polindrom(case18), 323)
    eq_(main.polindrom(case19), 323)
    eq_(main.polindrom(case20), 323)
    eq_(main.polindrom(case21), 323)
    eq_(main.polindrom(case22), 323)
    eq_(main.polindrom(case23), 323)
    eq_(main.polindrom(case24), 323)
