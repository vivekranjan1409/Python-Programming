# it is unordered
# it is mutable
# it is indexed
# it cannot contain duplicate keys  



myDict = {
    "Fast": "In a Quick manner",
    "Vivek": "a Coder",
    "marks": [1,2,3,4,5],

    "anotherDict": {"Vivek": "Player"}    #Nested Dictionary
}

# print(myDict)

# print(myDict["Fast"])
# print(myDict["Vivek"])
myDict["marks"] = [23,45,89]
print(myDict["marks"])
print(myDict["anotherDict"]['Vivek']) #Player