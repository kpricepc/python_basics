import unittest

#from unittest.case import _AssertRaisesContext

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')
    def test_upper(self):
        self.assertEqual('word'.upper(), 'WORD')
    def test_strip(self):
        s = 'letterhead'
        self.assertEqual(s.strip('letter'))
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello', 'world']) 
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()