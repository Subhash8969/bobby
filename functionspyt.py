#FUNCTIONS:
#simple function named as greet user that prints a greeting
def greetings():
    """display a simple greeting"""
    print("hello")
  
#passing information to a function
def greetings(username):
    print("hello,"+username)
greetings("subhash")
    
#passing arguments
#1.positional arguments
'''def describe_pet(animal,petname):
    print("i have a "+animal)
    print("my " + animal +" name is " + petname.title()+".")
describe_pet("dog","jonny")'''
'''step-1:here the definition describe_pet needs type of animal and name of it.
   step-2:here in this step we printed that which type of animal we have.here dog
   had stored in parameter(animal) here dog is an argument.
   step-3:here in this step we printed the animal type and name of the animal.
   we can see in parameter animal we passed argument as dog and in another para-
   meter we passed the argument dog name as 'jonny'.from this we can know that we
   know that we are passing arguments to parameters.
   @here we can see we passed the arguments in same order as parameter.'''
#MULTIPLE FUNCTION CALLS:
#describe_pet("cat","kitty")
'''step-1:here from this we can know that we call the function multiple times
          by giving different arguments'''
#******************************************************************************

#DEFAULT VALUES:
'''def describe_pet(petname,animal="cat"):
    print("i have a "+animal)
    print("my "+animal+" name is "+petname)
describe_pet(petname="dolly")
when we writting we can define a default value for each parameter.
1.here i have given value to the parameter 'animal' as cat.'''
#*******************************************************************
#1.AVOIDING ARGUMENT ERRORS:
'''def describe_pet(animal,petname):
    print("i have a "+animal)
    print("my " + animal +" name is " + petname.title()+".")

describe_pet()
1.here python recognizes that some information is missing and shows the error while we run 
the program'''
#******************************************************************************
# RETURN VALUES:
# RETURNING A SIMPLE VALUE:
'''def names(first_name,last_name):
    full_name=(first_name+" "+last_name)
    return(full_name.title())
mr=names("ganthala","subhash")
print(mr)

step-1:here the definition takes the parameter first and last name
step-2:here the function combines the two names and leaves space b/w them.And
stores the result in full_name.
step-3:the value of full_name is converted to title case,and returns to callig
line.
step-4:here in this step the returned value is stored in varible mr'''
#*****************************************************************************
# RETURNING A DICTIONARY:
'''def names(first_name,last_name):
    full_name={first:first_name+" "+last:last_name}
    return full_name
mr=names("ganthala","subhash")
print(mr)

step-1:a function can return any kind of value you need including data
structures like lists and dictionaries.

step-2:the value of first name is stored with the key "first"
       the value of last name is stored with the key as "last"'''
#*******************************************************************************
# USING A FUNCTION WITH A WHILE LOOP:
'''def names(first_name,last_name):
    full_name=(first_name+" "+last_name)
    return(full_name.title())
while True:
    print("please tell me your name")
    print("(enter 'q' at any time to quit)")
    f_name=input("first name:")
    if f_name=="q":
        break
    l_name=input("last name:")
    if l_name=="q":
        break
    fname=names(f_name,l_name)
    print("hello, "+fname)'''
#***************************************
#PASSING LIST:
'''def greetings(names):
    """print a simple greeting to each user in the list."""
    for i in names:
        msg="hello, "+i.title()
        print(msg)
names1=["ganthala","subhash","roy"]
greetings(names1)
    
step-1:here we are defining greetings of names so python expects list of names
   which stores in the parameter names.
   step-2:we pass list of names and pass the list names1 to greetings.
   step-3:we can see the output that every name is greetind individually'''
#****************************************************************************

   





















    








