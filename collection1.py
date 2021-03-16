
#from collections import Counter
'''list=[1,1,1,1,2,2,2,3,3,3,3,4,4,4]
print(Counter(list))'''

'''a=("aaaabsbfnfbbbbbabsb")
print(Counter(a))'''


'''s="two boys are fighting with six boys for a girl"
s1=s.split()
print(Counter(s1))'''


'''#element function
b=[1,1,1,1,1,2,2,2,2,3,3,3,5,5]
print(Counter(b))
g=Counter(b)
#element function
#print(list(g.elements()))'''

'''#most_common function gives output in tuple format
#print(g.most_common())'''

'''#subtract function
s={1:3,2:2,3:1}
g.subtract(s)
print(g)'''

'''c=Counter(a=3,b=2,c=4)
print(sorted(c.elements()))'''


from collections import ChainMap

a={"n1":2,"n2":3}
b={"n3":3,"n4":4}
cm=ChainMap(a,b)
print(cm)


a={"n1":2,"n2":3}
b={"n2":3,"n4":4}
cm=ChainMap(a,b)
print(list(cm))

#print(cm["n1"])
#adding new dictionary to chain map
'''c={"n5":5,"n6":6}
ncm=cm.new_child(c)
print(ncm)'''


'''from collections import namedtuple

x=namedtuple("courses","name,language")
tp=x("datascience","python")
print(tp)
#using _asdict() function
t=tp._asdict()
print(t)
#_make() function
s2=x._make(["tough","ok"])
print(s2)'''

#from collections import deque
'''a=["s","u","b","h","a","s","h"]
g=deque(a)
g.appendleft("module")
print(g)'''
#removing elements from deque by pop() function
'''s=g.pop()
s=g.popleft()
print(g)'''

#clearing deque using clear()
'''lst=["a","b","c"]
s=deque(lst)
print(s)'''
#print(s.clear())
#counting elements in deque by count()
#print(s.count("b"))

'''from collections import OrderedDict
d=OrderedDict()
d[1]="s"
d[2]="u"
d[3]="b"
d[4]="h"
d[5]="a"
d[6]="s"
d[7]="h"
#print(d)
#print(d.keys())
#print(d.values())
#print(d.items())
#by using loop
for key,value in d.items():
    print(key,value)
#we used ordered dict with counter.here we create a counter from lis and
#insert element to orderdict based on their count
lst=[1,2,3,4,1,3,4,2,3,1,3]
c=Counter(lst)
od=OrderedDict(c.most_common())
for key,value in od.items():
    print(key,value)'''

'''from collections import defaultdict
#create a defaultdict
#you have to specify a data type
d=defaultdict(float)
d[1]="subbu"
d[2]="bobby"
print(d[3])
name="subbu bobby subbu bobby subbu roy roy ganthala".split()
for i in name:
    d[i]+=1
print(d)'''






