'''for x in range (6,0,-1):
    for g in range(x):
        print("*",end="")
    print("\n")'''
#******************************        
'''for x in range(6):
    for i in range(x+1):
        print("*",end="")
    print()'''
#******************************
'''for i in range(1,4):
    for a in range(1):
        print("*###*",end="")
    print("\n")'''
#*****************************
'''for r in range(5):
    for c in range(5):
        if (c==0 or c==4) or ((r==0 or r==4) and (c>0 and c<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()'''
#*******************************
'''sum=int(input("enter a number"))
for i in range(sum):
    sum=sum+i
    print(sum)'''
#*******************************
'''a=1
b=100
for j in range(1,101):
    if j>1:
        for i in range(2,j):
            if(j%i)==0:
                break
        else:
            print(j)'''
#*************************************
'''string1=input("enter a name")
if(string1==string1[::-1]):
    print("it is a palindrome")
else:
    print("not a palindrome")'''
#*************************************

'''list1=int(input("enter a list"))
list2=[]
for i in range(list1):
    a=int(input("enter an element"))
    list2.append(a)
print(list2)'''
'''sum=0
for j in range(list1):
    sum=sum+list2[j]
print(sum)'''
#*************************

'''a=int(input("enter a list"))
a1=[]
for i in range(a):
    a3=int(input("enter an element"))
    a1.append(a3)
print(a1)
sum=0
for j in range(a):
    sum=sum+a1[j]
print(sum)'''
#***********************************
s=("subhash")
l=len(s)
#print(l)
for i in range(l-1,-1,-1):
    print(s[i],end="")
#******************************************
'''s=[1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    if(i%2!=0):
        print(i+1)'''
#*************************
'''a=int(input("enter a list"))
a1=[]
for i in range(a):
    a2=int(input("enter an element"))
    a1.append(a2)
print(a1)               
for j in range(a):
    if(j%2!=0):
        print(j+1)'''
#*************************

'''for j in "subhash":
    if j=="b":
        break
    print(j)'''
#**************************
'''for i in "subhash":
    if i=="b":
        continue
    print(i)
print("good")'''
#*****************************

























