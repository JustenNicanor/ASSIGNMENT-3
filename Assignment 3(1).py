def getname():
    _name = input("What is your name? ")
    return _name
def getage():
    _age = input("What is your age? ")
    return _age
def getaddress():
    _address = input("what is your address? ")
    return _address
def display(nameF, ageF, addressF):
     print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}")
name = getname()
age = getage()
address = getaddress()
display(name, age, address)

