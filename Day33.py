#enumerate in python


a = ['H','a','c','k','e','r','r','a','n','k']

# for i in enumerate(a):
#     print(i)
    

# f = ["apple",'banana','mango','guava']

# for index,item in enumerate(f):

#     print(index,item)

for index,item in enumerate(a,start=2):
    print(index,item)