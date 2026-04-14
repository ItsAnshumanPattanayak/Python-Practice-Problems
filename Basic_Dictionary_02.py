'''
Write an interactive Python script that continuously loops, asking the user to either 'insert' a record or 'quit'.
If the user types 'insert', sequentially prompt them for a unique ID, a property key, and a value.
Store this data safely in a nested dictionary where the unique ID maps to the inner key-value pair.
Ensure the program appends new records properly without overwriting the entire existing database.
Print the updated dictionary after each insertion, and display "Invalid Input" for any unrecognized commands.
'''
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
