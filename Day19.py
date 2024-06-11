#Tuples in python
t = (1,2,3,4)
print(t)
print(type(t))
tup = (1)
print(type(tup)) # return int becoz it consist only one value

tup = (1,)
print(type(tup)) #return tuple

#tup[0] = 90 # error

tup = (1,2,3,4,5,6,"TUshar")
print(tup)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[4::-2]) #return 5,3,1

print(len(tup))

if 6 in tup:
    print('yes')



tup2 = tup[5::-1]
print(tup2)