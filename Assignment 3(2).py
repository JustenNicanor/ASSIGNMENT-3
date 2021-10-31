def getapple():
    _apple = int(input("How many apples? "))
    return _apple
def getorange():
    _orange = int(input("How many oranges? "))
    return _orange
def getapple_price():
    _apple_price = 20
    return _apple_price
def getorange_price():
    _orange_price = 25
    return _orange_price
def gettotal_cost(apple, orange, appleprice, orangeprice):
    _total_cost = (apple*appleprice) + (orange*orangeprice)
    return _total_cost
def display(totalcostF):
    print(f"The total amount is {totalcostF}.") 
apple = getapple()
orange = getorange()
appleprice = getapple_price()
orangeprice = getorange_price()
totalcost = gettotal_cost(apple, orange, appleprice, orangeprice) 
display_ = display(totalcost)
