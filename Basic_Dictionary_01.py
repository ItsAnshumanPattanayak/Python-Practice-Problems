'''
Build a Python-based inventory manager that uses a while True loop to continuously accept user commands until 'q' is entered to quit. The script must maintain a dictionary and provide options to add entries ('a'), remove keys ('r'), list all keys ('gk'), list all values ('gv'), or display the full collection as formatted key-value pairs ('all'). Ensure the program handles unrecognized inputs by displaying an "Action is invalid" error message instead of crashing.
'''
my_dict = {}
while True :
    user = input("\nEnter your action\nAdd (a)\nRemove(r)\nget all key (gk)\nget all values (gv)\nSee all the items (all)\nquit(q)\n-->:")
    if user == "a" :
        a= input("Enter the key: ")
        b = input("Enter the value: ")
        my_dict[a] = b
        print(my_dict)
    elif user == "r":
        if c in my_dict:
            c = input("Enter the Key: ")
            del my_dict[c]
        else :
           print("Error: That key does not exist!") 
    elif user == "gk":
        print(my_dict.keys())
    elif user == "gv":
        print(my_dict.values())
    elif user == "all":
        for key,value in my_dict.items():
            print(f"{key}:{value}")
    elif user == "q" :
        break
    
    else:
        print("Action is invalid")
