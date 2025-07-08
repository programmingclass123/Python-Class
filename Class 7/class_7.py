# Things we learned

# Collections
# 1. List
# 2. Set
# 3. Tuple
# 4. Dictionary

# LIST

items = ["lays","fanta","biscuit"] 

for i in items: # i = 1
    print(i)

print(items)
print(items[2])

# adding item in the end
items.append("apple")
print(items)

# removing item from the end
items.pop()
print(items)

# updating specific item
items[0] = "popcorn"
items[1] = "pepsi"
print(items)

# arrange your items in alphabetic manner
items.sort()
print(items)

# arrage your items in 
items.reverse()
print(items)

# removing an item
items.remove("popcorn")
print(items)



# Clear your whole list
items.clear()
print(items)

