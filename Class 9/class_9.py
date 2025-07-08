# Things we learned
# Strings

text = "Lays fanta grocery salt sugar"

print(text.capitalize())

print(text.casefold())


print(text.strip())

print(text.upper())

print(text.lower())

print(text.split())

test = input("write your name: ") # ali
uppercase = test.capitalize() # ALI
for i in range(5):       
    if uppercase == "Ali":  # ali is equal to ALI
        print("your name is ali")
    else:
        print("your name is not ali")

    test = input("write your name: ")