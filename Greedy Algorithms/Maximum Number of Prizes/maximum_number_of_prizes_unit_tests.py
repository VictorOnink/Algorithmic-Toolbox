import unittest
from maximum_number_of_prizes import compute_optimal_summands


class MaximumNumberOfPrizes(unittest.TestCase):
    def test(self):
        for (n, answer) in [(1, 1), (6, 3), (100, 13), ]:
            summands = compute_optimal_summands(n)
            self.assertEqual(len(summands), answer)
            self.assertEqual(sum(summands), n)
            summands = sorted(summands)
            self.assertTrue(all(summands[i] < summands[i + 1] for i in range(len(summands) - 1)))

        for n in range(1,100):
            print("i = {}, summands = {}".format(n,compute_optimal_summands(n)))

if __name__ == '__main__':
    unittest.main()
