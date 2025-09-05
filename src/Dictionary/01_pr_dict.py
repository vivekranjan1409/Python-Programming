myDict ={
    "pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}

print("Options are: ",myDict.keys())
a = input("Enter the hindi word: ")
print("The meaning of the word is: ",myDict[a]) # this line will thrown an error if the key is not present in the dictinary
print("The meaning of your word is: ", myDict.get(a))  # this line will not thrown the error if the key is not present in the dictionary