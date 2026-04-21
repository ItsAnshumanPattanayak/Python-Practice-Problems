# Write a Python program to calculate the total cost of items in a customer's shopping cart.
def calculate_total_cost(cart):
    total_cost = 0 
    for item in cart :
        total_cost+= item['price']*item['quantity']
    return total_cost
cart = [
    {'name' : 'Apple' , 'price' : 10, 'quantity' : 4},
    {'name' : 'Oranges' , 'price' : 8, 'quantity' : 3},
    {'name' : 'Grapes' , 'price' : 15, 'quantity' : 5},
    {'name' : 'Watermelon' , 'price': 50, 'quantity' : 8}
]
c= calculate_total_cost(cart)
print(c)