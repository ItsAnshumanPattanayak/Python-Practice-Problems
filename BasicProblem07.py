'''
Write a Python program for a cinema's digital ticketing system that calculates 
prices based on age and student status. Toddlers (under 5) are Free, children 
(5–12) pay Rs 150, and seniors (over 50) pay Rs 500. For those aged 13–17, the 
price is Rs 200 for students and Rs 250 for others, while those aged 18–50 pay 
Rs 300 if they are students and Rs 350 otherwise. Your code must accept age (integer) 
and student status (y/n) as inputs, handle case sensitivity for the status, and output 
the final ticket price clearly
'''
age = int(input("Enter your age :"))
is_student = input("Are you a student ( y / n )").lower()

# Using conditional statetement
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
