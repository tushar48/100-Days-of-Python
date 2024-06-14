#f - string

print("Hello")
print(f'Hello {None}')

a = "This is a good {1} {0}"
p = "Platform"
p2 = "Platform2 "
print(a.format(p2,p))



price = 23.232343423
txt = f"This is value {price : .2f}"
print(txt)


print(f"{2*10}")
f = "value"
print(f"this is {{f}}")
