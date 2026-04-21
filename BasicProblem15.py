'''
create a class "Programmer" for sorting infomation of few programmers 
working at microsoft
'''
class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , job_role):
        self.name = name 
        self.salary = salary
        self.job_role = job_role

p = Programmer("Anshuman" , 100000 , "AI/ML Engineer")
print(p.name , p.salary , p.job_role , p.company)
q = Programmer("Ashutosh" , 200000 , "Senior Software Engineer")
print(q.name , q.salary , q.job_role , q.company)
