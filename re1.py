import re
#findall()
'''str="subbu"
x=re.findall("b",str)
print(x)'''
#search()
'''s="bobby roy"
g=re.search("roy",s)
print(g)'''

#split()
'''s="bobby roy"
g=re.split("r",s)
print(g)'''

#sub()
'''s="bobby roy"
g=re.sub("r","b",s) #where ever the given pattern matches r is replaced by b
print(g)'''
#[]
'''s="hello subhash how are you"
g=re.findall("[how]",s)
print(g)'''
#^
'''s="hello subhash how are you"
g=re.findall("^hello",s)
print(g)'''

#$
'''s="hello subhash how are you"
g=re.findall("u$",s)
print(g)'''

#.
'''s="hello subhash how are you"
g=re.findall(".h",s)
print(g)'''

#*
'''s="hello subhash how are you"
g=re.findall("h*",s)
print(g)'''

#+
'''s="hello subhash how are you"
g=re.findall("h+",s)
print(g)'''

#{}

'''s="hello subhash how are you"
g=re.findall("l{2}",s)
print(g)'''

#\s
'''s="hello subhash how are you"
g=re.findall("\s",s)
print(g)'''

#\S
'''s="hello subhash how are you"
g=re.findall("\S",s)
print(g)'''

#\d
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("\d",s)
print(g)'''

#\D
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("\D",s)
print(g)'''

#\w
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("\w",s)
print(g)'''

#\W
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("\W",s)
print(g)'''

#SETS
#[123]
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("[123]",s)
print(g)'''

#[^abc]
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("[^abc]",s)
print(g)'''

#[a-z]
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("[a-z]",s)
print(g)'''

#[0-9]
'''s="1 2 3 5 hello subhash how are you"
g=re.findall("[0-9]",s)
print(g)'''

#[0-9] [0-9]
'''s="1235 hello subhash how are you"
g=re.findall("[0-9][0-9][0-9][0-9]",s)
print(g)'''











