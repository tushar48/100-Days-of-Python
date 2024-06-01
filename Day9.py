#string methods


a = "     Tushar"
#strings are immutable i.e it cannot be changed but change differently. Existing string cannot be changed but make a new one then change it

# print(a)
# print(len(a))
# print(a.upper())
# print(a.lower())



print(a.strip())
print(a.rstrip(" "))
print(a.lstrip(" "))


print(a.replace("Tushar","Uchiha"))

print(a.split(","))

name = 'clan'

print(name.capitalize())

print(name.center(50))


x = "Madara"
# print(len(x))
# print(len(x.center(50)))

# print(x.count('a'))

# print(x.endswith('s'))


# print(x.endswith('ra',3,6))


# print(x.find('r'))

# print(x.index('a'))


print(x.isalnum()) # a-z A-Z

print(x.isalpha())

print(x.islower())
x = "kuchbhi\n"
print(x.isprintable()) 

print(x.isspace())


print(x.istitle())

print(x.swapcase()) #a-Z A-z

print(x.title())













