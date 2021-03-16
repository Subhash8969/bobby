'''class vendingmachine:
    def __init__(self):
        pass
    def items(self):
        item1={"coke":[1,20,5],"thmsp":[2,25,3],"sprite":[3,30,6]}
        print("select 1 for coke")
        print("select 2 for thmsp")
        print("select 3 for sprite")
        userinput=int(input("select items from 1,2,3:"))
        for i,j in item1.items():
            if userinput==j[0]:
                print("you have selected",i)
                qnt=int(input("required quantity:"))
                if qnt<=j[2]:
                    g=qnt*j[1]
                    print("price of the item is:",g)
                    myamnt=float(input("enter amount:"))
                    if myamnt<g:
                        print("required more money")
                    else:
                        change=myamnt-g
                        print("remaining money is:",change)
                else:
                    print("no stock")        
            
b=vendingmachine()
b.items()'''
#*************************************************
class vendingmachine:
    def __init__(self):
        pass
    def items(self):
        item1={"coke":[1,20,8],"thmsp":[2,25,10],"sprite":[3,30,15],"fanta":[4,35,20],"lays":[5,20,50]}
        print("select 1 for coke")
        print("select 2 for thmsp")
        print("select 3 for sprite")
        print("select 4 for fanta")
        print("select 5 for lays")
        userinput=int(input("select items from 1,2,3,4,5:"))
        for i,j in item1.items():
            if userinput==j[0]:
                print("you have selected:",i)
                qnt=int(input("required quantity is:"))
                if qnt<=j[2]:
                    g=qnt*j[1]
                    print("price of the item is:",g)
                    rq=j[2]-qnt
                    print("remaining stock is:",rq)
                    myamnt=float(input("enter amount:"))
                    if myamnt<g:
                        print("required more money")
                    else:
                        change=myamnt-g
                        print("remaining money is:",change)
                else:
                    print("no stock")
                






b=vendingmachine()
b.items()
