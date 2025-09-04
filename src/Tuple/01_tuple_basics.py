# creating a tuple using ()
# Access tuple items using indexing 
# Tuples are immutable - we cannot change items in a tuple
# Tuples can contain items of different data types
# we can create a tuple with item of different data types
# we can slice a tuple using : operator
# tuple indexing starts from 0 and goes to n-1 where n is the number of items in the tuple
tuple1 = (1,2,3,4,5)
# tuple1[0] = 10  # this will raise an error because tuples are immutable
print(tuple1[0])
print(tuple1[0:3])
# print(tuple1[5::-1])  # this will raise an error because index 5 is out of range
tuple2 = ("Vivek", 1, 2.5, True)
print(tuple2)
print(type(tuple2))
print(len(tuple2))
# we can create a tuple without using ()    
tuple3 = 1,2,3,4,5
print(tuple3)
print(type(tuple3))



# we can create a tuple with one item by adding a comma after the item
tuple4 = (1,)
print(tuple4)
print(type(tuple4))


# we can unpack a tuple into variables
a,b,c,d,e,f = tuple4
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# we can use tuple() constructor to create a tuple from an iterable (like list, string, etc.)
tuple5 = tuple(["Vivek", "Raushan", "Rohit"])
print(tuple5)
tuple6 = tuple("Vivek") # string is an iterable
print(tuple6)
# we can use count() method to count the number of occurrences of an item in a tuple
print(tuple4.count(3))
# we can use index() method to find the index of the first occurrence of an item in a tuple