myDict = {
    "Fast": "In a Quick manner",
    "Vivek": "a Coder",
    "marks": [1,2,3,4,5],

    "anotherDict": {"Vivek": "Player"},    #Nested Dictionary
    1:2
}

# Dictionary Methods

print(type(myDict))

# Key method 
print(myDict.keys())  # print all the keys of the dictionary
print(list(myDict.keys()))  #Typecasting

# Values Method
print(myDict.values())   # print all the values of the dectionary
print(list(myDict.values())) #TypeCasting


# Item Method
print(myDict.items())  # prints the (key,value) for all contents of the dictionary

updateDict = {
    "luv": "kush",
    "Vivek":"A Dancer"
}

# Update Method

myDict.update(updateDict);  # Updates the dictionary by adding key-value pairs from updateDict.
print(myDict);

# Get Method
print(myDict.get("Vivek"));
print(myDict.get("Vivek1"));   # Returns none as Vivek1 has not present in the dictionary

print(myDict["Vivek"]);
# print(myDict["Vivek1"]);   throws an error as Vivek1 has not present in the dictionary


