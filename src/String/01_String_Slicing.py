greet = "Good Morning, "
name = "Vivek"

# Concatination two strings
c = greet + name
print(c)
# print(greet + name)
# print(greet*3)
# print(greet[0])

# Slicing string 
print(greet[0:4])  # 0 to 4-1 = 3
print(greet[0:5])  # 0 to 5-1 = 4
print(greet[0:6])  # 0 to 6-1 = 5
print(greet[:3]) # 0 to 3-1 = 2 by default start with 0
print(greet[3:]) # 3 to end by default end
print(greet[::1]) # start to end by default start with 0 and end with len-1 and jump 1 index
print(greet[::2]) # start to end by default start with 0 and end with len-1 and jump 2 index


name = "Vivek Ranjan"
print(name[0:-1:2])