''' Greedy Algorithms: Example 3 - Fractional Knapsack '''

class Item:
    ''' Represents our fractionable things to put in the Knapsack'''
    def __init__(self, name=None, price=0, portion=0):
        self.name = name
        self.portion = portion
        self.price = price
        if portion != 0:
            self.cost = price / portion

    # make it sortable by cost
    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return str(self.price) + "," + str(self.portion)

def get_max_price(things, knapsack_size):
    ''' Gets the maximum value that can fit in the knapsack'''

    if knapsack_size <= 0:
        return 0

    total_value = 0
    current_wt = 0

    # now the things are sorted by cost
    things.sort(reverse=True)
    for thing in things:
        # take the whole item with the highest cost ratio and add them to the total value
        if current_wt + thing.portion <= knapsack_size:
            current_wt = current_wt + thing.portion
            total_value = total_value + thing.price
        # until we can’t add the next item as a whole, only a fraction to fill the capacity
        else:
            remaining_wt = knapsack_size - current_wt
            total_value = total_value + thing.price * (remaining_wt / thing.portion)
            break

    return total_value

def main():
    ''' Example Input '''
    # Here are flour bags of all sorts, with a given (name, price, weight)
    things = [Item("almond", 60, 10), Item("rice",100,20), Item("tapioca",120, 30)]

    # Here's a knapsack to carry your stuff, it can carry up to this much weight
    knapsack_size = 50

    # Get the most money for the knapsack capacity you have
    max_value = get_max_price(things, knapsack_size)
    print ("Max Value: ", max_value)

if __name__ == "__main__":
    main()
