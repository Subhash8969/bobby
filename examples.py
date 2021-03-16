#Basic programs:
#adding two numbers:
'''s=14
b=2198
g=s+b
print(g)'''
#*****************************
#maximum numbers:
'''a=14
b=2198
maximum=max(a,b)
print(maximum)'''
#*******************************
#factorial number
'''num=7
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial)'''
#*********************************
#prime numbers:
'''s=1
g=30
for i in range(s,g+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)'''
#*********************************
'''list1=[2,4,5,7,8,9,6,3,1]
no1=[]
while list1:
    min=list1[0]
    for x in list1:
        if x<min:
            min=x
    no1.append(min)
    list1.remove(min)
print(no1)'''

















