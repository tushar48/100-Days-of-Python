#set methods


a = {1,2,3,4,5} 
b = {4,5,6}

# a.update(b)
print(a)

print(b.union(a))

print(a,b)


#by using update method set will update itself 
#in union that set itself will not update rather than it will make another set and put values on it

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.isdisjoint(b))

print(a.issuperset(b))

a.discard(2)
a.discard(9)
print(a)

item = a.pop()
print(item)

del a
# print(a)
