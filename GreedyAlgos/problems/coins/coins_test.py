''' Greedy Algorithms: Example 2 - Giving change unit tests'''
import unittest

give_change = __import__("coins").give_change

gbp_coin_denominations = [2, 1, .10, .50, .20, .01, .02, .05]

class TestGiveChangeGBPDenominations(unittest.TestCase):
    ''' Tests using the GBP coin denominations '''

    def test_give_change_float(self):
        ''' Input is a sum of a possible combination of coins '''
        change = 0.67
        bag_of_coins = give_change(change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins,4)

        sum_of_all_coins = 0
        for coin in bag_of_coins:
            sum_of_all_coins = sum_of_all_coins + coin
        self.assertEqual(sum_of_all_coins, change)

    def test_give_change_equal_to_a_denomination(self):
        ''' Input is a value equal to a denomination '''
        one_coin_change = 0.50
        bag_of_coins = give_change(one_coin_change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins, 1)
        self.assertEqual(bag_of_coins[0],0.50)

    def test_give_change_greater_than_biggest_denomination(self):
        ''' Input is a value greater than the biggest available denomination '''
        big_change = 3
        bag_of_coins = give_change(big_change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins, 2)

        sum_of_all_coins = 0
        for coin in bag_of_coins:
            sum_of_all_coins = sum_of_all_coins + coin
        self.assertEqual(sum_of_all_coins, big_change)

    def test_give_change_negative_number(self):
        ''' Input is a value less than zero '''
        negative_change = -0.67
        bag_of_coins = give_change(negative_change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins, 0)

    def test_give_change_zero_number(self):
        ''' Input is zero '''
        empty_change = 0
        bag_of_coins = give_change(empty_change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins, 0)

    def test_give_change_none(self):
        ''' Input is None '''
        nil_change = None
        bag_of_coins = give_change(nil_change, gbp_coin_denominations)
        num_of_coins = len(bag_of_coins)
        self.assertEqual(num_of_coins, 0)


if __name__ == '__main__':
    unittest.main()
