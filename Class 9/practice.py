strings = input("Write a string: ")

count = 0

for i in strings:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count = count + 1

print (count)