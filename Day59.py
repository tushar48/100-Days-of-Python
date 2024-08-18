#Decorator in python

print("Decorator")


def greet(func):
    def funcx():
        print("Good Morning")
        func()
        print("THanks for using this functions")
    return funcx
@greet    
def hello():
    print("Hello bro")


def add():
     hello()

# greet(hello)()

 