t = (1,2,4,5,4,1,2,1,1)

print(t)

# count() - returns the number of occurrences of an item in a tuple
print(t.count(1))   

# index() - returns the index of the first occurrence of an item in a tuple
print(t.index(4))

# we can use index() method with optional start and end parameters to specify the range to search for the item
print(t.index(1,2,7))  # search for 1 between index 2 and 7
