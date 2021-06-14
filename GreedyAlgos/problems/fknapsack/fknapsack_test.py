''' Greedy Algorithms: Example 3 - Fractional Knapsack Tests'''
import unittest

fknapsack = __import__("fknapsack")

class TestGetMaxPrice(unittest.TestCase):
    ''' Tests get_max_price() '''

    def test_get_max_price_partial_final_item(self):
        ''' The remaining capacity of the knapsack has to be filled
        with a fraction '''
        items = [fknapsack.Item("almond", 60, 10),
                fknapsack.Item("rice",100,20),
                fknapsack.Item("tapioca",120, 30)]
        capacity = 50
        max_price = fknapsack.get_max_price(items,capacity)
        self.assertEqual(max_price, 240)

    def test_get_max_price_perfect_items(self):
        ''' The items perfectly fit the capacity '''
        items = [fknapsack.Item("almond", 60, 10),
                fknapsack.Item("almond", 100, 10)]
        capacity = 20
        max_price = fknapsack.get_max_price(items,capacity)
        self.assertEqual(max_price, 160)

    def test_get_max_price_zero_weight_knapsack(self):
        ''' Knapsack can't hold anything '''
        items = [fknapsack.Item("almond", 60, 10)]
        capacity = 0
        max_price = fknapsack.get_max_price(items,capacity)
        self.assertEqual(max_price, capacity)

    def test_get_max_price_zero_weight_item_zero_price(self):
        ''' Items that do not have a weight '''
        items = [fknapsack.Item("almond", 0, 0)]
        capacity = 10
        max_price = fknapsack.get_max_price(items,capacity)
        self.assertEqual(max_price, 0)
