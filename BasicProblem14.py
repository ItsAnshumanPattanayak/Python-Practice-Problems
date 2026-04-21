'''
Write a Python program to demonstrate a class with a constructor,instance 
methods, class variables, and a static method using a Soap class that displays 
product details.
'''

# with 2 funtions
class Soap :
  company1 = "Lux"
  cost1 = "50"

  company2 = "Dettol"
  cost2 = "100"

  def __init__(this): # __init__() is a dunder method which is automatically called
    print("Welcome!! ** This is a constructor **")

  def lux_soap (this) : # function 1
    print(f"The cost of {this.company1} is {this.cost1}")

  def dettol_soap (this) :# function 2
    print(f"The cost of {this.company2} is {this.cost2}")

  @staticmethod
  def greet (): #function 3
    print("Good Morning") 

fetch_soap = Soap()
fetch_soap.greet()
fetch_soap.lux_soap()
fetch_soap.dettol_soap()
