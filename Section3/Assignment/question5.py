list =  [("Lambert", 34, 10.50), ("Osborne", 22, 6.25), ("Giacometti", 5, 100.70)]

print("{: >10} {: >10} {: >10}".format("Name", "Hours", "Pay"))
for x in list:
    print("{: >10} {: >10} {: >10.2f} $".format(*x))