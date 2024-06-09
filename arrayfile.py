#Sourab Shukla Array and List

from array import *


a = array('i',[1,2,3,4,5,6,7,8,9,10]) #i signed integer and I unsigned Integer
print(a)

for i in a:
    print(i)

print(type(a))

b = array('I',[1,2,4])


print(b)

for x in range(len(b)):
    print(b[x])

i = 0
while(i < len(a)):
    print(a[i])
    i+=1
    



a.append(12)

print(a.count(10))

a.remove(5)
print(a)

