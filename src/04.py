import os
a = 4
b = 'Vivek'
c = 3.7
d = True
e = None    

print('Hello' , 'World')
print(a,b)
print(a)
print(b)
print(c)        
print(d)
print(e)

print(type(a))
print(type(b))      
print(type(c))
print(type(d))
print(type(e))

if a > c:
    print("a is greater than c")
else:
    print("a is less than c")

x=y=z = "vivek"
print(x)
print(y)
print(z)

print("Enter your name:")
name = input()

print("Hello "+name)
print("Hello",name)
print(f"Hello {name}")


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
print("Sum is: ", a+b)
print("Difference is: ", a-b)   
print("Product is: ", a*b)
print("Quotient is: ", a/b)

print("Remainder is: ", a%b)
print("Floor Division is: ", a//b)
print("Exponent is: ", a**b)

choice = input("Enter your choice (1 for addition, 2 for subtraction , 3 for multiplicarion , 4 for division , 5 for modulo): ")
if choice == '1':
    print("Sum is: ", a+b)
elif choice == '2':
    print("Difference is: ", a-b)
elif choice == '3':
    print("Product is: ", a*b)
elif choice == '4':
    print("Quotient is: ", a/b)
elif choice == '5':
    print("Remainder is: ", a%b)
else:
    print("Invalid choice")



    
