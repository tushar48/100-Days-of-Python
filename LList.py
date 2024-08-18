#Singly Linked List Code

class LL:
    def __init__(self,node=None,next=None):
        self.node = node
        self.next = next

    def getvalue(self):
        return self.node


i = 0
a = LL()
temp = a
while(True):
    if i == 0:
        val = int(input())
        if val == -1:
            break
        i += 1
        a.node = val
        a.next = None
    else:
        val = int(input())
        if val == -1:
            x = LL(val)
            a.next = x
            a = a.next
            break
        x = LL(val)
        a.next = x
        a = a.next








# while(temp.node != -1):
#     print(temp.node,end=' ')
#     temp = temp.next






print("Insertion Part Comes")

val = int(input())
k = LL(val,temp)
temp = k


while(temp.node != -1):
    print(temp.node,end=' ')
    temp = temp.next






# a = LL(None,None)
# temp = a
# while(True):
#     first = int(input())
#     if(first == -1):
#         break
#     x = LL(first)
#     a.next = x
#     a = a.next


# #Insertion
# print("Insertion Part Begins")

# val = int(input())
# N = LL(val,None)
# N.next = temp
# N = temp

# while(temp.next != None):
#     print(temp.node,end=' ')
#     temp = temp.next