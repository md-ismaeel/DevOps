print("HI! Enter Your Name")
name = input()
print(type(name))
print("Your Name is " + name)

marks=int(input("Enter Your Marks"))
print(type(marks))
# print("Your Marks are " + str(marks))

if marks >= 90:
    print("You Got A+")
elif marks >= 80:
    print("You Got A")
elif marks >= 70:
    print("You Got B")
elif marks >= 60:
    print("You Got C")
elif marks >= 50:
    print("You Got D")
else:
    print("You Got F")
    