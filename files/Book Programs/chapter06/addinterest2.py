# addinterest2.py
#    Illustrates use of return to change value in calling program.

def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print amount

test()

