#nested dictionary problem 
my_dict = {}
while True:
    user = input("\nWhat you want to do : Insert or Quit: ")

    if user == "insert":
            id = input("\nEnter your id name:")
            key = input("\nEnter your key:")
            value = input("\nEnter your value:")

            my_dict = {
                id : {key : value}
            }
            print(my_dict)
    elif user == "quit":
            break
    else:
            print("\nInvalid Input")
