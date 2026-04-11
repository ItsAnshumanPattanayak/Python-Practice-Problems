'''Design and implement a menu-driven calculator application in Python  
that performs basic arithmetic operations using functions.'''
def sum():
    a = int(input("Enter your number 1:"))
    b = int(input("Enter your number 2 :"))
    addition = a+b
    print( "The sum of" , a , "and", b , "is" ,  addition) 

def minus():
    a = int(input("Enter your number 1:"))
    b = int(input("Enter your number 2 :"))
    substract = a-b
    print("The subtract of" , a , "and", b , "is" , substract)

def multiply():
    a = int(input("Enter your number 1:"))
    b = int(input("Enter your number 2 :"))
    multiplication= a*b
    print("The multiplication of" , a , "and", b , "is" , multiplication)
    
def divide():
    a = int(input("Enter your number 1:"))
    b = int(input("Enter your number 2 :"))
    division = a/b
    print("The Division of" , a , "and", b , "is" , division)

print("Welcome to my Calculator")

while True :
    action =input("+ , - , * , / , q : ")


    if action == '+' :
        sum()
    elif action == '-':
        minus()
    elif action == '*':
        multiply()
    elif action == '/' : 
        divide()
    elif action == 'q':
        print("Thanks for using ")
        break
    else :
        print("Invalid action")
