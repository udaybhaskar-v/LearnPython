#Reading The number from input
num=int(input("enter a number"))
#diclaring and initializing the variable factorial
factorial =1
#if statement
if num < 0:
   print "factorial can't be evaluated for negative values";
   
elif num == 0:
   print "the factorial of 0 is 0";
else:
#for loop 
   for val in range(1, num+1):
      factorial=factorial * val
print "factorial of", num, "is" ,factorial
