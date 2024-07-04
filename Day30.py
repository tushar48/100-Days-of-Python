print("Clean Up")

def func():

    try:
        l = [1,2,3,4]
        c = int(input())
        print(l[c])
        return 1
    except:
        print("Some error occured")
        return 0

    finally:
        print("This is the finall code")


x = func()
print(x)




