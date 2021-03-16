from abc import ABC,abstractmethod
class abstractdemo(ABC):#abstractdemo is a subclass for ABC &it is abstract class
    @abstractmethod       #abstract methods
    def display(self):
        None
    @abstractmethod      #abstract methods
    def show(self):
        None
class demo2(abstractdemo):#it is an derived class of abstract class
    def display(self):    #it is also abstract class because only one method is
                           #overrided
        print("abstract method")
class demo3(abstractdemo):   #cocrete class because all methods are implemented
    def show(self):
        print("subhash")
    def display(self):
        print("display")
c=demo3()
c.display()
    
