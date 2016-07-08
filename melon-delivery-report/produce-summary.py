#function that prints out amount from selling melons with file as argument 
def calc_melon_dollars(file): 
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()

#Call function for day 1 report
print "Day 1"
calc_melon_dollars("um-deliveries-20140519.txt")

#Call function for day 2 report
print "Day 2"
calc_melon_dollars("um-deliveries-20140520.txt")

#Call function for day 3 report
print "Day 3"
calc_melon_dollars("um-deliveries-20140521.txt")

