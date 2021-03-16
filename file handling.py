file=open("new.txt","w")
file.write("hello subhash")
file.close()
file=open("new.txt","a")
file.write(" i am not okay")
file.write("\n but fine")
file.close()
file=open("new.txt","r")
print(file.read())
file.close()

file=open("new.txt","r")
print(file.readline(4))



