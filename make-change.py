import unittest

# Calculate the number of ways to make change
def change_possibilities(amount, denominations):
    if amount == 0: # there's only one way to make change of zero cents
        return 1
    else:
        ways_to_reach_n_cents = [0] * (amount + 1)
        ways_to_reach_n_cents[0] = 1 # there's 1 way to make 0 cents.

        for coin in denominations: # loop through the possible coins to use
            for amount in range(coin, amount + 1): # these are the indices of ways_to_reach_n_cents.
                # we know the amount of ways to get all the change less than the current amount with the given coin
                remainder = amount - coin
                ways_to_reach_n_cents[amount] += ways_to_reach_n_cents[remainder]

        return ways_to_reach_n_cents[amount]


# Tests
class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
