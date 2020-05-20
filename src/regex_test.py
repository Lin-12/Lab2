import unittest
from shunting_yard import convert
from thompsons import run_thompson
from r_e import reg_match, check_concat
from collections import OrderedDict


class ThompsonsTest(unittest.TestCase):
    def test_shunting(self):
        postfix = convert("(a.b)|(c*.d)")
        print("Convert (a.b)|(c*.d) to postfix: " + postfix)
        self.assertEqual(postfix, "ab.c*d.|")

        postfix = convert("(a.b+)|(c*.d)")
        print("Convert (a.b+)|(c*.d) to postfix: " + postfix)

    def test_thompson(self):
        print("Test function but no visualization on NFA object: " + run_thompson("ab.cd.|").__str__())

    def test_regex(self):
        string_list = ["", "abc", "abbc", "abcc", "abad", "abbbc"]
        infix_result = OrderedDict([
                                ("a.b.c*", [False, True, False, True, False, False, False]),
                                ("a.(b|d).c*", [False, True, False, True, False, False, False]),
                                ("(a.(b|d))*", [True, False, False, False, True, False, False]),
                                ("a.(b.b)*.c", [False, False, True, False, False, False, False]),
                                ("a.b+.c*", [False, True, True, True, False, True, False])
                                ])

        for i in infix_result:
            for s in string_list:
                self.assertEqual(reg_match(i, s), infix_result[i][string_list.index(s)])
                print("Match \"%s\" to \"%s\" is: %s" % (i, s, reg_match(i, s)))

    def test_regex_case(self):
        self.assertTrue(reg_match("A.B.C*", "aBCCccCC", True))
        print("Match case insensitive \"%s\" to \"%s\" is: %s"
              % ("A.b.C*", "aBCCccCC", reg_match("A.B.C*", "aBCCccCC", True)))

        self.assertFalse(reg_match("A.B.C*", "aBCCccCC"))
        print("Match case sensitive \"%s\" to \"%s\" is: %s"
              % ("A.b.C*", "aBCCccCC", reg_match("A.B.C*", "aBCCccCC", False)))

    def test_regex_concat(self):
        self.assertEqual(check_concat("abc|(de).f"), "a.b.c|(d.e).f")
        print("Add concat operator \"%s\": \"%s\"" % ("abc|(de).f", "a.b.c|(d.e).f"))


if __name__ == '__main__':
    unittest.main()