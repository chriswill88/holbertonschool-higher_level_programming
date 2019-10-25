import unittest
import pep8
from models.rectangle import Rectangle


"""
This modual contains class TestRect:
"""


class TestRect(unittest.TestCase):
    """
    Class TestRect : testing class for Rectangle modual
    """
    def testpep8(self):
        """ pep8 test """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/rectangle.py'])
        print(r.total_errors, "total errors")
        self.assertEqual(r.total_errors, 0, "found code errors and warnings. ")


if __name__ == '__main__':
    unittest.main()
