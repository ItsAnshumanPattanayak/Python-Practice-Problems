#password strength checker 
user = input("\nEnter your Password: ")
def is_strong_password(user):
    if len(user)<6:
        return False
    if not any(char.isdigit() for char in user):
        return False # change this 
    if not any(char.islower() for char in user):
        return False # change this
    if not any (char.isupper() for char in user):
        return False# change this
    if not any (char in '!@#$%^&*()_+' for char in user):
        return False # change this
    return True
c = is_strong_password(user)
print(c)
# add more functions like low , medium ,high 