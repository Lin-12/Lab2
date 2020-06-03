import unittest
from regex import *

class  RegEx(unittest.TestCase):

    # test regular expression +
    def test_plus(self):
        st = "bbbb"
        pat = "b+"
        result = Regex(st, pat).match_All()
        self.assertEqual(st, result)

    #test regular expression *
    def test_multiplication(self):
        st = "aaaa"
        pat = "a*"
        result = Regex(st, pat).match_All()
        self.assertEqual(st, result)

    #test regular expression |
    def test_or(self):
        st = "abbbb"
        pat="\*?|ab+"
        result = Regex(st, pat).match_All()
        self.assertEqual(st, result)

    #test regular expression .
    def test_point(self):
        st = "hello"
        pat= "hel.o"
        result = Regex(st, pat).match_All()
        self.assertEqual(st, result)

    # test regular expression ^
    def test_start(self):
        st = "zzzzzz"
        pat = "^z*"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, st)
    # test regular expression $
    def test_end(self):
        st = "xxxxx"
        pat = "^x*$"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, st)


    # test my email
    def test_email(self):
        st = "zzz2510555317@qq.comdfsfsdf"
        pat="^2510555317@qq.com"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, "2510555317@qq.com")
        st = "bbbbjlemon-0615@163.combbbb"
        pat = "^lemon-0615@163.com"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, "lemon-0615@163.com")

    # test name
    def test_filename(self):
        st="/hello/huangyanlinnnn/linningningggg"
        pat="/hello/huangyanlin+/linningning+"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, st)

    #test phone number
    def test_phone_number(self):
        st="aaa13888111110"
        pat = "^138+1*0$"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, "13888111110")
    # test failure case
    def test_fail(self):
        st = "qbcdefss"
        pat = "a+"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, "ERROR")
        st = "aaa13888111110"
        pat = "cv2*"
        result = Regex(st, pat).match_All()
        self.assertEqual(result, "ERROR")

if __name__=="__main__":
    unittest.main()