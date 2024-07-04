#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

#Nested List
# student = [['A',12],['B',13],['C',13],['D',12],['E',10]]
# def solve(student_list):
#     marks = []
#     for i in student_list:
#         marks.append(i[1])
#     marks = sorted(set(marks))
#     second_lowest = marks[1]
#     answer = []
#     for i in student_list:
#         if i[1] == second_lowest:
#             answer.append(i[0])
#     answer = sorted(answer)
#     for i in answer:
#         print(i)


# solve(student)

#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

# print("%.2f" % (sum(student_marks[query_name]) / 3))

#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true


# s = input()   


# s = sorted(s, key = lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))
# print(*s, sep="")

#https://www.hackerrank.com/challenges/python-lists


# n = int(input())
# ans = []
# for i in range(n):
#     command,*nums = input().split()
#     match command:
#         case "insert":
#             ans.insert(nums[0],nums[1])
#         case "print":
#             print(ans)
#         case "remove":
#             ans.remove(nums[0])
#         case "append":
#             ans.append(nums[0])
#         case "sort":
#             ans.sort()
#         case "pop":
#             ans.pop()
#         case "reverse":
#             ans.reverse()


#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true


# input_string = input()
# n = int(input_string)
# tuple_elements = input().split()
# tuple_result = tuple(map(int, tuple_elements))
# print(tuple_result)
# print(tuple_result.__hash__())
# print(tuple_elements)


# string = "Hello"
# char_list = list(string)
# toggled_list = [char.lower() if char.isupper() else char.upper() for char in char_list]

# print("".join(toggled_list))

# https://www.hackerrank.com/challenges/python-string-split-and-join

#    return "-".join(line.split(" "))

#https://www.hackerrank.com/challenges/find-a-string

# string = "ABCDCDCDC"
# substring = "CDC"

# sublen = len(substring)

# i = 0
# j = sublen
# cnt = 0
# while i < j and j < len(string)+1:
#     if string[i:j] == substring:
#         cnt = cnt + 1
#     i = i + 1
#     j = j + 1

# print(cnt)


#https://www.hackerrank.com/challenges/maximize-it



# n, m = map(int, input().split())
# a = list
# res = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     res.append(a)


# print(res)

# lastlist = []

# for i in res:
#     # lastlist.append(max(i))
#     t = max(i)
#     lastlist.append(t*t)


# print(sum(lastlist)%m)


#https://www.hackerrank.com/challenges/string-validators


# s = input()    
# print(any(char.isalnum() for char in s))
# print(any(char.isalpha() for char in s))
# print(any(char.isdigit() for char in s))
# print(any(char.islower() for char in s))
# print(any(char.isupper() for char in s))

# https://www.hackerrank.com/challenges/text-alignment


# w = 20
# print("Tushar".ljust(w,'-'))

# print("Tushar".center(w,'-'))

# print("Tushar".rjust(w,'-'))

# a = 'H'

# print(a.center(5,' '))
# print([a*3].center(5,' '))


# import textwrap


# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

# print(textwrap.wrap(string,4))

# print(textwrap.fill(string,4))


# print(5//2)
# print(6//2)

# thickness = 5
# c = 'H'

# for i in range(thickness):
#     print((c*i).rjust(thickness - 1) + c + (c*i).ljust(thickness - 1))

# for i in range(thickness + 1):
#     print((c*thickness).center(thickness * 2) + (c*thickness).center(thickness*6))

# for i in range((thickness + 1)//2):
#     print((c*thickness*5).center(thickness*6))
  

# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#https://www.hackerrank.com/challenges/designer-door-mat

# rows,cols = map(int,input().split())

# for i in range(rows//2):
#     print((".|."*(2*i + 1)).center(cols,'-'))

# print("WELCOME".center(cols,'-'))

# for i in range(rows//2):
#     print((".|."*(2*(rows//2 - i - 1) + 1)).center(cols,'-'))

# if sequence would be 1 3 5 7 --> (2n + 1)
# if sequence would be 7 5 3 1 --> (2*(last_value)*n - i - 1)





#https://www.hackerrank.com/challenges/python-string-formatting

# a = 15
# print(hex(a)[2:])
# print(oct(a)[2:])
# print(bin(a)[2:])

# for i in range(1,15):
#     print(str(i) + ' ' + oct(i)[2:].capitalize() + ' ' + hex(i)[2:].capitalize() + ' ' + bin(i)[2:].capitalize() + '\n')


# w = len(format(a,'b'))
# print(w)

# for i in range(1,16):
#     d = format(i,'d').rjust(w,' ')
#     o = format(i,'o').rjust(w,' ')
#     x = format(i,'x').rjust(w,' ').upper()
#     b = format(i,'b').rjust(w,' ')
#     print(f'{d} {o} {x} {b}')


# https://www.hackerrank.com/challenges/alphabet-rangoli

n = 5
# l1 = list(map(chr,range(97,123)))

# x = l1[n-1::-1]+l1[1:n]
# m = len('-'.join(x))


# # print('-'.join(x))

# for i in range(1,n):
#     print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))

# for i in range(n,0,-1):
#     print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))





# s = "hello world"

# l = s.split(' ')
# print(l)
# s2 = [word.capitalize() for word in l]
# print(s2)
# s2 = ' '.join(s2)
# print(s2)



# https://www.hackerrank.com/challenges/the-minion-game

# s = "BANANA"
# s length is 6 total substring would be 21 --> n*(n+1)/2 
#based on the criteria we can differentiate the strings 
# kev = 0
# stu = 0

# for i in range(len(s)):
#     if s[i] in ['A','E','I','O','U']:
#         kev += len(s) - i
#     else:
#         stu += len(s) - i
# print(kev,stu)

#https://www.hackerrank.com/challenges/itertools-product
# from itertools import product

# a = [1,2,3]
# b = [3,4,5]


# a = list(map(int,input().split(' ')))
# b = list(map(int,input().split(' ')))
# #print(list(product(a,b)))
# for item in list(product(a,b)):
#     print(item,sep=' ',end=' ')

# from collections import Counter

# mylist = [1,1,1,2,3,3,2,2,3,2,4,1,2,3,23,1,3,231,23,231]


# print(Counter(mylist))

# print(Counter(mylist).items())

# print(Counter(mylist).keys())

# print(Counter(mylist).values())


# no_of_shoe = int(input())

# shoe_size = list(map(int,input().split()))

# no_of_customers = int(input())

# customers = []
# for i in range(no_of_customers):

#     customer = list(map(int,input().split()))

#     customers.append(customer)

# print(customers)

# print(Counter(shoe_size))

# amount = 0

# for i in customers:
#     if i[0] in Counter(shoe_size):
#         # amount += i[1] * Counter(shoe_size)[i[0]]
#         amount += i[1]
#         shoe_size.remove(i[0])

# print(amount)

#https://www.hackerrank.com/challenges/itertools-permutations/

# from itertools import permutations

# print(list(permutations([1,2,3])))

# print(list(permutations([1,2,3,4],1)))

# print(list(permutations("abc",2)))

# s = "ACBD"

# s = sorted(s)
# print(s)

# print(list(permutations(s,2)))
# ans = list(sorted(permutations(s,2)))
# print(ans)

# a = "\n".join([i[0]+i[1] for i in ans])

# for i in ans:
#     print(*i,sep="")

# print(a)


#https://www.hackerrank.com/challenges/itertools-combinations
    
# from itertools import combinations


# print(list(combinations([1,2,3,4],2)))

# A = [1,1,3,3,3]

# print(list(combinations(A,4)))





# S , K = input().upper().split()

# k = int(K)

# result = []
# for i in range(1 ,k + 1):
#     result.extend(combinations(sorted(S) , i))

# print(result)
# for j in result:
#     print(''.join(j))


#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement



# from itertools import combinations_with_replacement

# print(list(combinations_with_replacement('12345',2)))

# A = [1,2,4,1,3,1]

# print(list(combinations_with_replacement(A,2)))

# S , K = input().upper().split()

# k = int(K)

# result = []
# for i in range(1 ,k + 1):
#     result.extend(combinations_with_replacement(sorted(S) , i))

# print(result)
# for j in combinations_with_replacement(sorted(S) , k):
#     print(''.join(j))


# import cmath

# print(cmath.phase(complex(-1.0,0.0)))

# print(abs(complex(-1.0,0.0)))


#set
# print(set())
# print(set("HackerRank")) #always give different result
# print(set("HackerRank") == set("HackerRanK")) #Always False


# print(set([1,2,1,2,3,4,5,6,7,12,22,3]))

# print(set((1,2,3,4,5,5)))

# print(set(set(['H','a','c','k','e','r','r','a','n','k'])))

# print(set({"Hacker":"DOSHI","RANK":818})) #always give different output

# print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))

# n = int(input())

# arr = list(map(int,input().split()))

# s = set(arr)
# print(sum(s)/len(s))


# a = input()
# lis = a.split()
 # print(lis)


# newlis = list(map(int,lis))

# print(newlis)


# myset = {1,2}
# myset = set()
# myset = set(['a','b'])
# print(myset)

# myset.add('c')
# print(myset)

# myset.add('a')

# print(myset)

# myset.add((5,4))
# print(myset)

# myset.update([1,2,3,4])
# print(myset)

# myset.update({1,2,3})
# print(myset)

# myset.update({1,6},[5,13])
# print(myset)

# a = {2,4,5,9}
# b = {2,4,11,12}
# print(a.union(b))

# print(a.intersection(b))

# c = a.difference(b)
# d = b.difference(a)

# print(sorted(d.union(c)))


# a = int(input())
# s1 = set(map(int,input().split()))
# b = int(input())
# s2 = set(map(int,input().split()))

# c = s1.difference(s2)
# d = s2.difference(s1)

# ans = sorted(c.union(d))
# for i in ans:
#     print(i)



# print(a.union(b) == b.union(a))

# print(a.intersection(b) == b.intersection(a))

# print(a.difference(b) == b.difference(a))
#https://www.hackerrank.com/challenges/defaultdict-tutorial
# from collections import defaultdict

# d = defaultdict(list)
# d['python'].append('awesome')
# print([i for i in d.items()])

# d['something-else'].append("not relevant")
# d['python'].append('language')

# for i in d.items():
#     print(i)
# from collections import defaultdict

# n, m = list(map(int, input().split()))
# A = defaultdict(list)

# for i in range(n):
#     A[input()].append(str(i+1))

# for i in range(m):
#     temp_word = input()
    
#     if A[temp_word]:
#         print(" ".join(A[temp_word]))
#     else:
#         print("-1")

# import calendar

# print(calendar.weekday(2020,5,14))
# a,b,c = input().split(' ')

# print(calendar.day_name[0])


# a = 500
# b = 35.0
# res = a/b
# forres = "{:.3f}".format(res)
# print(forres,"km/l")


# import math
# x1,y1 = (input().split(' '))
# x2,y2 = (input().split(' '))
# x1 = float(x1)
# y1 = float(y1)
# x2 = float(x2)
# y2 = float(y2)
# x_res = x2 - x1
# y_res = y2 - y1

# x_res = x_res**2
# y_res = y_res**2

# over = x_res+y_res

# ans = math.sqrt(over)

# print("{:.4f}".format(ans))


# a,b,c = input().split(' ')
# d,e,f = input().split(' ')

# b = int(b)
# c = float(c)
# e = int(e)
# f = float(f)

# print("VALOR A PAGAR: R$","{:.2f}".format((b*c)+(e*f)))

# for _ in range(int(input())):
#     a,b = input().split(' ')
#     try:
#         print(int(a)//int(b))
#     except Exception as e:
#         print("Error Code:",e)

# print(eval('9 + 5'))
# x = 2
# print(eval('x + 12'))

# print(type(eval('len')))

# a = 'print(2 + 3)'
# eval(a)

# type(eval('3'))


# from collections import namedtuple

# p = namedtuple('Point','x,y')
# pt1 = p(1,2)
# pt2 = p(3,4)
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)

# print(dot_product)


from collections import namedtuple

# car = namedtuple('Car','Price Mileage Colour Class')
# xyz = car(Price=10000,Mileage=30,Colour='Red',Class='Y')
# print(xyz)

# car(Price=10000,Mileage=30,Colour='Blue',Class='O')
# print(car.Class)

n = int(input())

headers = input().split()

Student = namedtuple('Student',headers)

total_marks = 0

for i in range(n):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average = total_marks/n

print(f"{average:.2f}")

