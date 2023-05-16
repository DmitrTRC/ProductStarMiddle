import unittest
from Homeworks.HW2_SquareRoots import SquareRootEquation


class GetRootsTestCase(unittest.TestCase):
    def test_get_discriminant(self):
        self.assertEqual(SquareRootEquation.get_discriminant(1, 2, 1), 0)
        self.assertEqual(SquareRootEquation.get_discriminant(1, 2, 3), -8)
        self.assertEqual(SquareRootEquation.get_discriminant(1, 2, 4), -12)

    def test_get_roots(self):
        self.assertEqual(SquareRootEquation.get_roots(1, 2, 1), [-1])
        self.assertEqual(SquareRootEquation.get_roots(1, 2, 3), [])
        self.assertEqual(SquareRootEquation.get_roots(2, 3, -5), [1, -2.5])

        self.assertNotEquals(SquareRootEquation.get_roots(1, 2, 1), [1])
        self.assertNotEquals(SquareRootEquation.get_roots(1, 2, 3), [1, 2])


if __name__ == '__main__':
    unittest.main()
