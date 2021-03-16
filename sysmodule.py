#sys module
import sys
#print(sys.platform)
#print(sys.copyright)
#print(sys.version)
#print(sys.stdout.write("hello subbu"))
#print(sys.stderr.write("hello subbu"))
#a=["subhash",123456]
#print(sys.getsizeof(a[1]))
'''print("hello")
sys.exit()
print("bye")'''
#print(sys.path)
#print(sys.executable)
#print(sys.modules)
'''print(sys.argv)
import sys
print(sys.argv)
print(len(sys.argv))
for ele in sys.argv:
    print("arguments:",ele)'''
'''import sys
print(sys.argv)
print(len(sys.argv))
for i in range(0,len(sys.argv)):
    print("argument:",sys.argv[i])'''
'''#sum of all the elements from command line
import sys
sum=0
for i in range(1,len(sys.argv)):
    sum=sum+int(sys.argv[i])
print("result=",sum)'''


'''import sys
print(len(sys.argv))
for x in sys.argv:
    print(x)'''


'''import sys
mult=2
for i in range(1,len(sys.argv)):
    mult=mult*int(sys.argv[i])
print("result=",mult)'''

import sys
print(sys.getrecursionlimit())
'''interval=sys.getswitchinterval()
print("before changing,switchinterval=",interval)
interval=1
sys.setswitchinterval(interval)
interval=sys.getswitchinterval()
print("after changing,switchinterval=",interval)'''

#print(sys.maxsize)
#print(sys.getdefaultencoding())























    

