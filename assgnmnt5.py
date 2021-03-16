
'''s=[]
for i in range(0,30):
    i=i+1
    s.append(i)
print(s)
n=1
b=[]
while n<=len(s):
    if(n%2==0):
        b.append(n)
    n=n+1
print(b)
q=1
d=[]
while q<=len(s):
    if(q%2!=0):
        d.append(q)
    q=q+1
print(d)'''
#****************************************
'''lists=["apple rs 100/kg",
       "banana rs 5o/kg",
       "orange rs 40/kg"]
print(lists)
price=0
totalprice=0
items={"apple":100,"banana":50,"orange":40}
choose=int(input("for items press 1:"))
if choose==1:
    print(lists)
for i in range(len(items)):
    inp=int(input("if u want to buy press 1 0r 2 for return:"))
    if inp==2:
        break
    if inp==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            totalprice+=price
    print(price)
print("the total price of items is:",totalprice)'''
#*************************************************************************
'''def factors(x):
    for i in range(1,x+1):
       if x%i==0:
            print(i)
factors(126)
print(factors)'''
#*********************************

'''i=0
while i<5:
    i=i+1
    print(i)'''
#******************************

'''def square(num):
    return(num*num)
def cube(num):
    return(num**3)
    
num1=int(input("any number"))
sqr=square(num1)
print(sqr)

cub=cube(num1)
print(cub)'''
#***************************
'''def is_prime(num):
    for j in range(1,num):
        if j>1:
            for i in range(2,j):
                if(j%i)==0:
                    break
            else:
                print(j)
num1=int(input("enter"))
isprime=is_prime(num1)
print(isprime)'''
#****************************
'''def leng_strng(name):
    l=len(name)
    if l<5:
        print("length is less than 5")
    else:
        print("length is greater than 5")

leng_strng("subhash")'''     
#*****************************    
'''def multiple(num1,num2):
    for i in range(num2):
        #print(num1, " * ",i, "= ",num1*i)
        print(i*num1, end=" ")
multiple(5,1000)'''
#*************************************        
'''inputs= "today is saturday"
p=[]
for i in inputs:
    print(i,end=",")'''
#********************************
'''def types(num):
    print(type(num))
types("subhash")
types(0.2)
types(1)'''
#**********************************   
'''in_put=["green", "pink","white", "pink", "black","orange","red","blue","green", "green", "red","pink","pink", "orange"]
count={}
for x in in_put:
    if x in count.keys():
        count[x]=count[x]+1
    else:
        count[x]=1
print(count)'''
#***********************************************************

'''def is_palindrome(name):
    for i in range(len(name)):
        if name[i]!=name[len(name)-i-1]:
            return False
        return True
inpu_t=input("name")
pali=is_palindrome(inpu_t)
if pali:
    print("it is a palindrome")
else:
    print("no")'''
#*******************************************************




        
    
    
















