# Dictionaries method in python


a = {
    "Tushar" : "Human",
    "vage" : 12
}

print(a)

a.pop("Tushar")

print(a)

a.update({'vage': 25})
print(a)

a['Tushar'] = "Human"

print(a)

dic = sorted(a.keys())

print(dic)

sorted_dic = {i : a[i] for i in dic}

print(sorted_dic)

#a.clear()

#print(a)

a.popitem()

print(a)

#del is used for deleting the entire dictionary

