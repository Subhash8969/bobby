#EXCEPTIONS:
#HANDLING THE ZERO DIVISION ERROR FOR EXCEPTION
'''s=0
b=0
print(s/b)

#1.the error reported'''
#****************
'''def square1(num1):
    return (num1*num1)
in_put=int(input("numbers"))
sqr=square1(in_put)
print(sqr)'''


'''try:
    s=int(input("enter a number"))
    b=int(input("enter a name"))
    g=s/b
    print(g)
except:
    print("multiplication can't be done")
finally:
    print("thank you")'''
#****************************************************
'''try:
    a=10
    b=8
    c=a/b
    print(c)
except:
    print("can't divide")
finally:
    print("you got the answer")'''
#**************************************************************
'''amount=100
if (amount>99)
    print("ok done")'''
#*************************************************

'''try:
    age=12
    if(age<20):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("the age is not valid")'''

#********************************************
#Raise the exception as message
'''try:
    num1=int(input("enter a positive number"))
    if(num1<=0):
        raise ValueError("that is a negative number")
except ValueError as e:
    print(e)'''
#******************************************************
'''try:
    a=int(input("enter num:"))
    b=int(input("enter num:"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b=",a/b)
except ArithmeticError:
    print("the value of b can't be 0")'''
#****************************************************
import math
print(math.factorial(4))
help(math)























          
