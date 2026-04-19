lst = []
print("Welcome to the To-Do List Tracking :) Made by Anshuman Pattanayak Using python")

while True :

    main = input("\nChoose one of this action (add a task(add) , delete a task(delete), complete a task(complete) , check tasks (check), quit the application (quit)):\n")
    if main == 'add':
        

        #add tasks 
        while True:

            user= input("Press 'a' for adding tasks , 'q' for quit: ")

            if (user == 'a'):
                data = input("\nAdd Task :")
                lst.append(data)
                print(f"\n{data} was added to To-Do List\n")
                for i in lst :
                    print(i,end = " \n")
                print()
            elif (user == 'q'):
                # print("\nThanks for using this app:) Hope you like it\n")
                break
            else : 
                print("\nInavlid Input. TRY AGAIN!!\n")

    #remove task 
    if main == 'delete' :
        d = input("\nEnter the task that you want to delete\n")
        lst.remove(d)
        print(f"\n{d} has been removed\n")
        new = input("\nDid you want to enter a new task y/n ? :")
        if new == 'y':
            new_data = input("\nAdd New Task :")
            lst.append(new_data)
            print(f"\n{new_data} was added to To-Do List\n")
            for j in lst:
                print(j,end=" \n")
            print()
        elif new =='n':
            print("\nYour existing To-Do list is :\n")
            for k in lst:
                print(k,end=" \n")
        else : 
            print("\nInavlid Input. TRY AGAIN!!\n")