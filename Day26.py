#Dictionary

#Dictionary is an ordered collection of items

dic = {
    "Tushar" : "Human",
    "age" : 12
}

print(dic)
print(dic['age']) # if i entered age2 it will give me an error

#print(dic.get(input())) # if i entered age2 it will give me an None value


 
print(dic.get('Uchiha')) # retur None

print(dic.keys())

for key in dic.keys():
    print(key, dic[key])


print(dic.values())

print(dic.items()) # list of  tuples

for key,values in dic.items():
    print(key,values)





