"""

Test cases for alternation-characters in hackerrank

author: mishavietl

"""

from nose.tools import eq_

import main


def test_delete_copies():
    letters1 = "AAAA"
    letters2 = "AABAAAABBBB"
    letters3 = "A"
    letters4 = "B"
    letters5 = "AABAAA"
    letters6 = "AA"
    letters7 = "BB"
    letters8 = "BAAAB"
    letters9 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters10 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters11 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters12 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters13 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters14 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters15 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters16 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters17 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters18 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters19 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters20 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAA"
    letters21 = "AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBABAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBAAAAAAAAAAAAAAABABABABAAAAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBABABABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAABAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBAAAAAABBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBAAABBBBBBBBAA"



    eq_(main.delete_copies(letters1), 3)
    eq_(main.delete_copies(letters2), 7)
    eq_(main.delete_copies(letters3), 0)
    eq_(main.delete_copies(letters4), 0)
    eq_(main.delete_copies(letters5), 3)
    eq_(main.delete_copies(letters6), 1)
    eq_(main.delete_copies(letters7), 1)
    eq_(main.delete_copies(letters8), 2)
    eq_(main.delete_copies(letters9), 154)
    eq_(main.delete_copies(letters10), 154)
    eq_(main.delete_copies(letters11), 154)
    eq_(main.delete_copies(letters12), 154)
    eq_(main.delete_copies(letters13), 154)
    eq_(main.delete_copies(letters14), 154)
    eq_(main.delete_copies(letters15), 154)
    eq_(main.delete_copies(letters16), 154)
    eq_(main.delete_copies(letters17), 154)
    eq_(main.delete_copies(letters18), 154)
    eq_(main.delete_copies(letters19), 154)
    eq_(main.delete_copies(letters20), 154)
    eq_(main.delete_copies(letters21), 542)
