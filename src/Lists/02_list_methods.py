list = ["Vivek", "Raushan", "Rohit", "Ankit", "Vivek" ,"Sumit"]
print(list)

# append() - adds an item to the end of the list
list.append("Nitin")
print(list)

# insert() - adds an item at the specified index
list.insert(1, "Kumar")
print(list)

# remove() - removes the first item with the specified value
list.remove("Rohit")

print(list)

# pop() - removes the item at the specified index (default is the last item)
list.pop(2)
print(list)

# sort() - sorts the list in ascending order
list.sort()
print(list)

# reverse() - reverses the order of the list
list.reverse()  
print(list)

# copy() - returns a copy of the list
list2 = list.copy() 
print("List2 is : ",list2)

# count() - returns the number of items with the specified value
print(list.count("Vivek"))

# extend() - adds the elements of a list (or any iterable), to the end of the current list
list3 = ["Aman", "Suman"]
list.extend(list3)
print(list)

# index() - returns the index of the first item with the specified value
print(list.index("Vivek"))

# clear() - removes all the elements from the list
# list.clear()    
# print(list)

# del keyword - removes the item at the specified index or deletes the entire list
del list[0]  # deletes the first item

print(list)

# del list  # deletes the entire list
# print(list)  # this will raise an error because the list is deleted   
print(type(list))

# len() - returns the number of items in the list
print(len(list))