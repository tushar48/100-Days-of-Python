#List in Python

#List is an ordered collection of items

l = [1,2,3,4,5,6,7,8,9,10]

# print(l)
# print(type(l))

# print(l[0])

# l.append([1,2,4])
# print(l)

# l.extend([1,2,4]) #extend the list further with this parameter
# print(l)



print(l[-1])
print(l[len(l)-1])



# if 2 in l:
#     print("Yes")
# else:
#     print("No")





# if "sh" in "TUshar":
#     print("Yes")

# print(l)
# print(l[:])

# print(l[1:])
# print(l[1:-1]) #[1]


# print(l[4::-2])# explain this code?  l = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# print(l[6::-2]) # explain l = [1,2,3,4,5,6,7] -2 will be 7 - 2 = 5, 5 -2 = 3, 3 - 2 = 1
# answer would be --> 7,5,3,1


#l[start:stop:gap] if gap is negative then order goes into reverse and if gap is positive then order goes into the forward

lst = [i*i for i in range(4)]
lst = [i*i for i in range(10) if i%2 == 0]
 
print(lst)












