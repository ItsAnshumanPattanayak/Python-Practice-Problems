grades = []
while True:

    user = input("\nWhat action do you want to do : insert , add a new grade (new) ,average , find highest & lowest(type hl)\n")
    #inserting the grades 
    if user == 'insert':

        insert_grades = input("\nEnter the grades: ")
        grades = [insert_grades]
        print(f"Your grades are {grades}")
    #adding a new grade
    elif user == 'new':

        add_grade = input("\nEnter a new grade: ")
        print("\nYour new grade has been updated\n")
        grades=[add_grade]
        for i in grades:
            print(i,end=" \n")
        print()
    #average grade calculation
    elif user == 'average':

        average_grade = sum(grades) / len(grades)
        print(average_grade)
    elif user == 'hl':
        highest_grade = max(grades)
        lowest_grade = min(grades)
        print(f"The highest grade is {highest_grade}")
        print(f"The lowest grade is {lowest_grade}")
