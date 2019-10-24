import unittest
from models.rectangle import Rectangle
"""
This modual contains class TestRect:
"""


class TestRect(unittest.TestCase):
    """
    Class TestRect : testing class for Rectangle modual
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

if __name__ == '__main__':
    unittest.main()
