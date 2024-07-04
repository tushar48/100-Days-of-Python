#Error Handling

a = (input("Enter Number"))

# print(a*12)


try:
    print(int(a*12))

except:
    print("Enter Valid Number")



print("Kuch bhi")

try:
    n = int(input("Enter an integer: "))
    f = [4,3]
    print(n[f])
except ValueError:
    print("Number entered is not an integer")

except IndexError:
    print("Index error")

