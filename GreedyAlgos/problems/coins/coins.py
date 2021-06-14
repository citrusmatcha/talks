''' Greedy Algorithms: Example 2 - Giving change '''

def give_change(change, denominations):
    ''' returns a list of coins that make up the change in as few coins as possible '''

    bag_of_coins = []
    if change is None or change <= 0:
        return bag_of_coins

    denominations.sort(reverse = True)
    change = round(change, 2)

    while change:
        for coin in denominations:
            if change >= coin:
                change = round(change - coin, 2)
                print (change, coin)
                bag_of_coins.append(coin)
    return bag_of_coins


def main():
    ''' Example input '''
    # Welcome to the UK. Here are our coin denominations
    gbp_coin_denominations = set(2, 1, .50, .20, .10, .01, .02, .05)

    # Say we have an item for sale
    item_price = 4.33

    # And the customer gave us a GBP 5.00 note
    payment = 5.00

    # We need to give some change
    change = round(payment,2) - round(item_price,2)
    bag_of_coins = give_change(change, gbp_coin_denominations)
    print ("Your change: ", bag_of_coins)

if __name__ == "__main__":
    main()
