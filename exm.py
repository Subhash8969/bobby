#****************************************************************
class student:
    def __init__(self):
        pass
    f="pass"
      
            
    def details(self,name,science,maths,physics,hindi,english,social):
        self.name=name
        self.sb1=science
        self.sb2=maths
        self.sb3=physics
        self.sb4=hindi
        self.sb5=english
        self.sb6=social

        print("marks for science:",self.sb1)
        print("marks for maths:",self.sb2)
        print("marks for physics:",self.sb3)
        print("marks for hindi:",self.sb4)
        print("marks for english:",self.sb5)
        print("marks for social:",self.sb6)
        
    def pass1(self,passmark,a):
        f="pass"
        self.passmark=passmark
        self.passmark2=a
        
        if (self.sb1>=self.passmark):
            print("pass")
        else:
            print("fail")
            f="fail"
        if (self.sb2>=self.passmark):
            print("pass")
        else:
            print("fail")
            f="fail"
        if (self.sb3>=self.passmark):
            print("pass")
        else:
            print("fail")
            f="fail"
    
        if (self.sb4>=self.passmark2):
            print("pass")
        else:
            print("fail")
            f="fail"
            
        if (self.sb5>=self.passmark2):
            print("pass")
        else:
            print("fail")
            f="fail"
        if (self.sb6>=self.passmark2):
            print("pass")
        else:
            print("fail")
            f="fail"
        avg=(self.sb1+self.sb2+self.sb3+self.sb4+self.sb5+self.sb6)/6
        print("the average of marks:",avg)
                       
            
        total=(self.sb1+self.sb2+self.sb3+self.sb4+self.sb5+self.sb6)
        print("the total marks of student obtained out of 600 is:",total)
        
        if total>=550 and f!="fail":
            print("A grade")
        elif total>=400 and f!="fail" :
            print("B grade")
        elif total>=280 and f!="fail" :
            print("c grade")
        else:
            print("D grade fail")
            
       
                

        
g1=student()
s="y"
while s=="y":
    name=input("enter a name:")
    science=int(input("enter marks"))
    maths=int(input("enter marks"))
    physics=int(input("enter marks"))
    hindi=int(input("enter marks"))
    english=int(input("enter marks"))
    social=int(input("enter marks"))
    
    g1.details(name,science,maths,physics,hindi,english,social)
    g1.pass1(40,30)
    g1.f
    s=input("another student press y if n for no:")

#*******************************************************************



































































