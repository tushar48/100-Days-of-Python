# for loop with else statment


for i in range(2):
    if i == 1:
        break
    print(i)

else:
    print("Sorry no values in range")

# if break statement is there then else statement won't be work
# if break statement is not there then else statement will work

for i in []:
    print(i)


else:
    print("Sorry")