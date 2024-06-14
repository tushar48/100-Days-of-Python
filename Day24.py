#sets in python


a = {1,2,3,4,5}

print(a)

b = {2,3,4,5,6}

print(b)


print(a.union(b))


print(a.intersection(b))


#there is no maintaining of order


a.add(1)

print(a)



a.remove(1)
print(a)

s = set()

print(type(s))

for i in a:
    print(i)

