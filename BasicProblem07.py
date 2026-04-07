#Set the ticket price based on age and weather the person is a student or not
age = int(input("Enter your age :"))
is_student = input("Are you a student ( y / n )").lower()

#loops 
if age < 5:
    price = "Free"
elif age <= 12 :
    price = "Rs 150 ($1.61 )"
elif age <= 17 :
    if is_student == "y":
        price = "Rs 200 ($2.15 )"
    else:
        price  = "Rs 250 ($2.69 )"
elif age <= 50 :
    if is_student == "y":
        price = "Rs 300 ($3.23 )"
    else:
        price = "Rs 350 ($3.77 )"

else :
    price = "Rs 500 ($5.38 )"

print(f"The total price is : {price}")