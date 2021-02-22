import unittest
from primitive_calculator import compute_operations


class PrimitiveCalculator(unittest.TestCase):
    def test(self):
        for n, answer in ((2, 1), (3, 1), (5, 3), ):
            print(n)
            sequence = compute_operations(n)
            print('check length')
            self.assertEqual(answer, len(sequence) - 1)
            print('check first value')
            self.assertEqual(sequence[0], 1)
            print('check last value')
            self.assertEqual(sequence[-1], n)
            print('check order')
            for i in range(len(sequence) - 1):
                if sequence[i + 1] != sequence[i] + 1 and sequence[i + 1] != 2 * sequence[i]:
                    self.assertEqual(sequence[i + 1], 3 * sequence[i])


if __name__ == '__main__':
    unittest.main()
