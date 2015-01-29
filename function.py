# taking dynamic number of arguments to function
def myfunc(*lis):
    """return Even Values"""
    # filter takes function and list as arguments based on function boolean value it return the value from the list
    # lambda anonymous function
    new_list = list(filter(lambda x: (x%2 ==0), lis))
    print new_list	
# calling the function    
myfunc(22, 33, 44, 2, 3, 8, 9, 99, 41, 42, 88)
