#Write a Python program to determine if a given string is a palindrome
# s = input("Enter your string")
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
print(is_palindrome("a man a plan a canal panama"))
print(is_palindrome("Hello"))