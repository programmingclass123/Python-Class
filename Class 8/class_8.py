# Things we learned

# Functions

# Return Function
def sum(a, b, op): # a = 5, b = 7, op = +
    if op == "+": # op = + is equal to +
        c = a + b # c = 5 + 7 = 12, c = 12
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == "/":
        c = a / b
    else: 
        c = "invalid value"
    return c # c = 12

print(sum(5,7,"+")) # a = 5, b = 7, op = +
print(sum(2,8,"*"))
print(sum(4,9,"*"))
print(sum(8,2,"/"))


#Void Function
def grocery_list():
    items = ["rice", "sugar", "salt"]

    for item in items:
        print (item)


grocery_list()