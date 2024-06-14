#tuples method


t = (1,2,3,4)
l = list(t)
print(l)
l[-1] = "Hari"
t = tuple(l)
print(t)

t = (1,24,44,1,123,12,31,23,123,123,1,12,12,1,212)
print(t.count(123))

print(t.index(123)) #return 4
print(t.index(123,4,8)) # index(value,start,stop) 


