melon_cost = 1.00

def underpaid_customers(name, melons, paid):
    """ Determine if any client's paid amount is different from expected amount. """

    # to find the expected amount by multiplying melons by melon_cost
    expected = melons * melon_cost
    # print only the expected and the paid amount is different 
    if expected != paid:
        print name, "paid {:.2f}, expected {:.2f}".format(paid, expected)

#call functions on given people
underpaid_customers('Joe', 5, 5.00)
underpaid_customers('Frank', 6, 6.00)
underpaid_customers('Sally', 3, 3.00)
underpaid_customers('Sean', 9, 9.50)
underpaid_customers('David', 4, 4.00)
underpaid_customers('Ashley', 3, 2.00)

