def getmoneyamount():
    _money_amount = float(input("Enter your money amount: "))
    return _money_amount
def getappleprice():
    _apple_price =float(input("Enter the price of an apple you want: "))
    return _apple_price
def getappleamount(moneyamountF, applepriceF):
    _apple_amount= (moneyamountF / applepriceF)
    return _apple_amount
def getmaxapplesremmoney(moneyamountF, applepriceF):
    _max_apples_rem_money = (moneyamountF % applepriceF)
    return _max_apples_rem_money
def getdisplay(appleamountF, max_apples_rem_moneyF):
    print(f"You can buy {appleamountF} apples and your change is {max_apples_rem_moneyF} pesos.")

moneyamount = getmoneyamount()
appleprice = getappleprice()
appleamount = getappleamount(moneyamount, appleprice)
max_apples_rem_money = getmaxapplesremmoney(moneyamount, appleprice)
display = getdisplay(appleamount, max_apples_rem_money)

