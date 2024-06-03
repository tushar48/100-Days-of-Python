#Function arguement and return statement

def average(a=12,b=34):
    print(a) # a = 1
    print("Average is ",(a+b)/2)



average(7,92)
average()

average(b=2,a=1)


average(b = 3)

def avg2(*a):
    print(a) #  by default tuples dega
    # *a = Iterables 

    for i in a:
        print(i)

avg2([1,2,3,4,5,5,6])


def name(**name):
    print(name) #it will provide dictionary
    for i in name:
        print(i,name[i])


name(n = "tushar", lname = "Barnces")



def averages(*avg)->int:
    sum = 0
    for i in avg:
        sum += i

    return str(sum/len(avg))

print(type(averages(1,2,3,4,5,6,7,8,9,10)))

