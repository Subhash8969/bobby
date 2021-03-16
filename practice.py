'''import collections
a=[1,1,1,2,3,2,3,2,3,4,4,4]
print(collections.Counter(a))'''

#list comprehension
'''list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
pair=[(x,y) for x in (list1) for y in(list2) if x!=y ]
print(pair)'''

'''cube=[i**3 for i in range(10)]
print(cube)'''

#nested list comprehension
'''s=[[i for i in range(5)]for j in range(5)]
print(s)'''

'''s1=[1,2,3,4,5,6,7,8,9]
s2=[i for i in s1 if i%2==0]
print(s2)'''

#s1=[{"name":"subbu","age":23},{"name":"bobby","age":23}]
#s2=[]
#for i in s1:
    #s2.append(i["age"])
#print(s2)
#list comprehension
#s2=[i["age"] for i in s1]
#print(s2)

'''f=lambda a,b,c:a+b-c
r=f(3,4,5)
print(r)'''

'''def is_even(n):
    return n%2==0
n=[1,2,3,4,5,6,7]
even=list(filter(is_even,n))
print(even)'''

'''#filter()
n=[1,2,3,4,5,6,7]
even=list(filter(lambda s:s%2==0,n))
#map()
de=list(map(lambda s:s*2,even))
#print(even)
print(de)

from functools import reduce
sum=reduce(lambda s,b:s+b,de)
print(sum)'''


#iterator
'''def print_each(iterable):
    iterator=iter(iterable)
    while True:
        #try:
        item=next(iterator)
        #except StopIteration:
            #break
       # else:
        print(item)
s=print_each([1,2,3,"good","bad"])
print(s)'''

'''class looping:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return(val)
        else:
            raise StopIteration
val1=looping()

for i in val1:
    print(i)'''


#genarators
'''def gen():
    n=1
    yield n

    n=n+1
    yield n

    n=n+1
    yield n
a=gen()'''

'''print(next(a))
print(next(a))
print(next(a))
print(next(a))'''
'''for i in gen():
    print(i)'''


'''def all_even():
    n=0
    while True:
        yield n
        n=n+2
g=all_even()
print(next(g))
print(next(g))
for i in all_even():
    if i>300:
        break
    else:
        print(i)'''
'''s=[1,1,2,3,3,4,4,5,5,5]
d=[]
for i in s:
    if i not in d:
        d.append(i)
print(d)'''

'''m=["a","b","c","d"]
s=(dict.fromkeys(m))
print(s)'''













































