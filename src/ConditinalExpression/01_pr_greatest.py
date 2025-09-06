num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))
num4 = int(input("Enter Forth number: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("num1 is greater number")
elif(num2 > num3 and num3 > num4):
    print("num2 is greater.")
elif(num3 > num4):
    print("num3 is greater.")
else:
    print("num4 is greater")