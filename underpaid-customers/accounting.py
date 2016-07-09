melon_cost = 1.00

def customers_pay(name, melons, paid):
    """ Determine if any client's paid amount is different from expected amount. """

    # to find the expected amount by multiplying melons by melon_cost
    expected = melons * melon_cost
    # if customer underpaid 
    if expected > paid:
        print name, "paid ${:.2f}, expected ${:.2f} which is less than expected.".format(paid, expected)
    # if customer overpaid
    elif expected < paid: 
        print name, "paid ${:.2f}, expected ${:.2f} which is more than expected.".format(paid, expected)

#call functions on given people
customers_pay('Joe', 5, 5.00)
customers_pay('Frank', 6, 6.00)
customers_pay('Sally', 3, 3.00)
customers_pay('Sean', 9, 9.50)
customers_pay('David', 4, 4.00)
customers_pay('Ashley', 3, 2.00)

