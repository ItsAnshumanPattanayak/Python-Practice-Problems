## filter using lambda, functions , input

def greater(num5):
    greater_than_five = list(filter(lambda x:x>5,num5))
    print(greater_than_five)

user = input("\nEnter your list: ")
numbers2=list(map(int,user.split()))
greater(numbers2)