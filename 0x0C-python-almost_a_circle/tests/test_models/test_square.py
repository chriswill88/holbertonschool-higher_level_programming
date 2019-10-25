import unittest
import pep8
from models.square import Square

"""
This modual contains class TestBase:
"""


class TestSquare(unittest.TestCase):
    """
    Class TestSquare : testing class for Square modual
    """
    def testpep8(self):
        """ pep8 test """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/square.py'])
        print(r.total_errors, "total errors")
        self.assertEqual(r.total_errors, 0, "found code errors and warnings. ")


if __name__ == '__main__':
    unittest.main()
