import unittest
from majority_element import majority_element, majority_element_naive


class TestMajorityElement(unittest.TestCase):
    def test_small(self):
        for elements in [
            [7, 2, 7],
            [7, 8, 9],
            [2, 3, 2, 3],
            [1, 2, 3, 4],
            [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
        ]:
            self.assertEqual(
                majority_element(list(elements)),
                majority_element_naive(elements)
            )

    def test_large(self):
        for (elements, answer) in [
            ([0] * 5000 + [1] * 5000, 0)
        ]:
            self.assertEqual(
                majority_element(elements),
                answer
            )


if __name__ == '__main__':
    unittest.main()
