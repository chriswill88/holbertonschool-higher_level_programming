import unittest
from models.base import Base
"""
This modual contains class TestBase:
"""


class TestBase(unittest.TestCase):
    """
    Class TestBase : testing class for base modual
    """
    def test_base(self):
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
