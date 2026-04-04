# Find the largest of three numbers
a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
c= int (input("Enter the 3rd number :"))

if (a>b and a>c):
    print(a,"is the largest number")
elif (b>a and b>c) :
    print(b, "is the largest number")
elif (c>a and c>b) :
    print(c, "is the largest number")
else:
    print("Inavlid input")