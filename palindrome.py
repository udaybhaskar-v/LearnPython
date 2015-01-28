my_str = input("enter the string: ")
str2 = reversed(my_str)
if list(my_str) == list(str2):
    print ( "entered string is palindrome" )
else:
    print ("entered String is not palidrome")
