# addinterest1.py
#    Program illustrates failed attempt to change value of a parameter

def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    balance = newBalance

def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print amount
    
test()


