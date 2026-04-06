'''
write a class "calculator" capable of finding square, cube and square root of a number
'''

class calculator:
    
    user = int(input("Enter your number : "))

    def sqaure(self):
        print(f"The square of {self.user} is {self.user**2}")

    def cube(self):
        print(f"The cube of {self.user} is {self.user**3}")

    def squ_rt(self):
        print(f"The square root of {self.user} is {self.user**0.5}")

fetch_calc = calculator()

while True :
    print("\nWhat would you like to calculate?")
    print("1. Square\n2. Cube\n3. Square Root\n4. All\n5.Quit")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        fetch_calc.sqaure()
    elif choice == '2':
        fetch_calc.cube()
    elif choice == '3':
        fetch_calc.squ_rt()
    elif choice == '4':
        fetch_calc.sqaure() 
        fetch_calc.cube()
        fetch_calc.squ_rt()
    elif choice == '5':
        print("Thank you for using")
        break
    else:
        print("Invalid Input")