# Creating an empty set
a = set()

# Adding values to an empty set
a.add(3)
a.add(3)
a.add(3)
a.add(4)
a.add(4)
a.add(4)
a.add(4)
a.add(4)

# a.add([1,2,3,4,5]) in set we cannot add lists because of mutable concept of the list

a.add((1,2,3,4,5))  # in set we can be add tuples element
# a.add({2:3})   in set we cannot add dictionary also 

print(a)

# Operations on Sets
print(len(a))  # print length of the set

a.remove(3)   # removes 3 from the sets
print(a)

print(a.pop())
print(a)

a.clear() # emptities the sets
print(a)




