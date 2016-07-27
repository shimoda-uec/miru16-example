"""
Testing miru16.math module.
"""

try:
    import unittest2 as unittest
except:
    import unittest

import miru16.math as m

class TestCore(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(m.sub(1, 2), -1)

    def test_mul(self):
        self.assertEqual(m.mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(m.div(4, 2), 2)
        self.assertRaises(ZeroDivisionError, m.div, 4, 0)

    def test_mod(self):
        self.assertEqual(m.mod(3, 2), 1)
        self.assertRaises(ZeroDivisionError, m.mod, 3, 0)

if __name__ == '__main__':
    unittest.main()
