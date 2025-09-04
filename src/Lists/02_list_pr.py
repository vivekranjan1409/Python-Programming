math = int(input("Enter a marks of math: "))
chemistry = int(input("Enter a marks of Chemistry: "))
phy = int(input("Enter a marks of Physics: "))
eng = int(input("Enter a marks of English: "))
hin = int(input("Enter a marks of Hindi: "))
san = int(input("Enter a marks of Sanskrit: "))

Marks = [math, chemistry, phy, eng, hin, san]
Marks.sort()
print(Marks)