s = {18, "18"}

print(s)
print(len(s))


s1 = set()

s1.add(20)
s1.add(20.0)
s1.add("20")

# in python 20 and 20.0 is equal 

print(s1) # {'20',20}
print(len(s1)) # 2