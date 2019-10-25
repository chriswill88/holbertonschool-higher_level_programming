import unittest
import pep8
from models.base import Base

"""
This modual contains class TestBase:
"""


class TestBase(unittest.TestCase):
    """
    Class TestBase : testing class for base modual
    """
    def test_bid(self):
        """
        test method for Base.id
        """
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base()
        self.assertEqual(b.id, 3)

    def testpep8(self):
        """ pep8 test """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/base.py'])
        print(r.total_errors, "total errors")
        self.assertEqual(r.total_errors, 0, "found code errors and warnings. ")

if __name__ == '__main__':
    unittest.main()
