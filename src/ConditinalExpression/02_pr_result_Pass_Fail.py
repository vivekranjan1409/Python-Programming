sub1 = int(input("Enter the marks of subject1: "))
sub2 = int(input("Enter the marks of subject2: "))
sub3 = int(input("Enter the marks of subject3: "))

marks = (sub1 + sub2 + sub3) / 3
# print(marks)

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail. because you have less than 33 percent in one of the subject")

elif(marks < 40):
    print("you are fail due to total percentage less than 40.")
else:
    print("Congratulation! you are passed.")