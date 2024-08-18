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


# from collections import namedtuple

# car = namedtuple('Car','Price Mileage Colour Class')
# xyz = car(Price=10000,Mileage=30,Colour='Red',Class='Y')
# print(xyz)

# car(Price=10000,Mileage=30,Colour='Blue',Class='O')
# print(car.Class)

# n = int(input())

# headers = input().split()

# Student = namedtuple('Student',headers)

# total_marks = 0

# for i in range(n):
#     student_data = input().split()
#     student = Student(*student_data)
#     total_marks += int(student.MARKS)

# average = total_marks/n

# print(f"{average:.2f}")

# from collections import OrderedDict

# di = {}

# di['a'] = 1
# di['b'] = 2
# di['c'] = 3
# di['d'] = 4
# di['e'] = 5

# print(di)

# odi = OrderedDict()

# odi['a'] = 1
# odi['b'] = 2
# odi['c'] = 3
# odi['d'] = 4
# odi['e'] = 5

# print(odi)


# n = int(input())
# dicts = OrderedDict()
# for i in range(n):
#     item = input().split()
#     key = ' '.join(item[0:len(item)-1])
#     value = int(item[len(item)-1])
#     if key in dicts:
#         dicts[key] += value
#     else:
#         dicts[key] = value
# for item in dicts:
#     print(item,dicts[item])




# s = set("Hackerank")
# s.add('H')

# print(s)

# print(s.add("Hackerank"))
# print()

# s = set([1,2,3,4,4,5,6,7,8,9,9])
# s.remove(5)
# print(s)

# print(s.remove(4))
# print(s)

# s.remove(1)

#remove method raises an error if the finding element is not there
#discard method won't raise an error if the finding element is not there

# s.discard(0)
# print(s)

#pop wil remove first element

# s.pop()

# print(s)
# s.pop()
# print(s)

# s.pop()

# print(s)

# a = input().split()

# print(a)
# print(a[0])

# s = set("Hacker")
# print(s.union("Rank"))

# print(s.union(set(['R','a','n','k'])))

# print(s.union(enumerate(['R','a','n','k'])))

# print(s.union({"Rank":2}))

# print(s | set("Rank"))

# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {10, 1, 2, 3, 11, 21, 55, 6, 8}

# print(b.difference(a))

# print((b.symmetric_difference(a)))



# from collections import deque

# d = deque()

# d.append(1)

# print(d)

# d.appendleft(2)

# print(d)

# d.clear()

# print(d)

# d.extend('1')
# print(d)

# d.extendleft('123')
# print(d)

# d.count('1')

# print(d.count('1'))


# d.pop()

# print(d)

# d.popleft()

# print(d)

# s = deque(map(int,input().split()))

# print(s)

# print(divmod(177,10)[0])

# for i in range(1,int(input())):
#     print(i*(10**i)//9)


# / --> means floor division
# // --> means round off division

#Maths Pattern for Printing Concepts
# for i in range(1,11):
#     print(i*(10**i)//9)

#https://codeskiller.codingblocks.com/problems/170

# n = int(input())
# for i in range(n):
#     s = input().split()
#     a = s[0]
#     b = s[1]
#     i = 0
#     j = 0

#     while i<len(a) or j < len(b):
#         print(int(a[i]) ^ int(b[j]),end="")
#         i+=1
#         j+=1
    
#https://codeskiller.codingblocks.com/problems/218

#first approach

# a = [4,0,2,0,5,6,7,0]

# cnt = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         a[cnt] = a[i]
#         cnt += 1
# while cnt < len(a):
#     a[cnt] = 0
#     cnt+=1

# for i in range(len(a)):
#     print(a[i],end=" ")


#second approach
#l = 0
# for i in range(len(a)):
#     if a[i]:
#         a[l],a[i] = a[i],a[l]
#         l+=1

        
# for i in range(len(a)):
#     print(a[i],end=" ")
    

# print([1,2,3]*2)

# a = set("Hacker")
# b = set("rank")

# # a.update(b)

# print(a)
# # a.intersection_update(b)

# print(a)

# a.difference_update(b)

# print(a)

# a.symmetric_difference_update(b)
# print(a)




# from collections import Counter
# a = [1,3,2,1,3,1,2,3,3,3,2,1,1,2,2,9]
# k = 5

# c = Counter(a)
# size = len(a)//k
# print(size)
# print(c)
# for item in c:
#     if c[item] == 1:
#         print(item)

# a = set([ 8, 5, 6, 3, 2, 1, 4, 7])
# b = set([2])

# print(b.is(a))

#any() --> return true if any element in iterable is true otherwise return false

# print(any([1>0,1==0,1<0]))

#all() --> return true if all the elements of the iterable are true otherwise false

# print(all(['a'<'b','b'<'c']))
# l = [12,19,61,15,14]
# ans = any(str(i) == str(i)[::-1] for i in l)
# print(ans)

#Didn't Understood this below code

# def calculate_pairs(N, M):
#     # Maximum pairs
#     max_team_size = N - M + 1
#     max_pairs = (max_team_size * (max_team_size - 1)) // 2
    
#     # Minimum pairs
#     q, r = divmod(N, M)
#     min_pairs = r * (q * (q + 1)) // 2 + (M - r) * (q * (q - 1)) // 2
    
#     return min_pairs, max_pairs

# # Example usage
# N = 5  # Number of participants
# M = 1   # Number of teams
# min_pairs, max_pairs = calculate_pairs(N, M)
# print(f"Minimum pairs: {min_pairs}")
# print(f"Maximum pairs: {max_pairs}")



# Matrix Multiplication

# import numpy
# n = int(input())

# A = numpy.array([list(map(int,input().split())) for i in range(n)])

# B = numpy.array([list(map(int,input().split())) for i in range(n)])

# print(numpy.matmul(A,B))




# def isarm(n1):
# 	numlen = len(str(n1))
# 	i = 0
# 	s = 0
# 	tempn1 = n1
# 	while i < numlen:
# 		temp = n1%10
# 		s += pow(temp,numlen)
# 		n1 = n1//10
# 		i+=1

# 	if s == tempn1:
# 		print(tempn1)

# n1 = int(input())
# n2 = int(input())

# while n1 <= n2:

# 	isarm(n1)
# 	n1+=1


# mini = 0
# maxi = 100
# step = 20


# for i in range(mini,maxi+1,step):
# 	ans = (5/9)*(i - 32)
# 	print(i,'\t',int(ans))

# import numpy

# print(numpy.zeros((3,3,3)))
# print(numpy.ones((3,3,3)))

# n = input()
# length_of_n = len(n)
# num = int(n)
# l = [0]*length_of_n
# cnt = 0
# while(num > 0):
# 	rem = num%10
# 	cnt+=1
# 	l[rem - 1] = cnt
# 	num = num//10

# ans = int(''.join(map(str,l)))

# print(ans)

#Inverse of a number
	
# n = int(input())
# ans = 0
# i = 1
# while(n > 0):
# 	rem = n%10
# 	ans += i*pow(10,rem-1)
# 	n = n//10
# 	i+=1
# print(ans)



# n = (input())
# length = len(n)
# n = int(n)
# temp = n
# s = 0

# while(n > 0):
# 	rem = n % 10
# 	s += pow(rem,length)
# 	n = n//10

# if (s) == temp:
# 	print("true")
# else:
# 	print("false")


#https://codeskiller.codingblocks.com/problems/3460

# n = int(input())
# a = list(map(int,input().split()))

# s = 0
# curr = 1
# for i in range(len(nums)):
# 	s += nums[i]
# 	curr = min(s,curr)

# if curr > 0:
# 	return 1
# else:
# 	return -1*curr + 1


# import numpy

# a = [1,2,3,4]

# arr = numpy.array(a)
# print(arr.reshape(2,2))

# S = "welcome to geeksforgeeks"

# S = "".join([i for i in S if i not in 'aeiou'])
# print(S)




# a = "13X357-22"
# first = a[0:2]
# second = a[3:6]
# third = a[7:]
# length = len(first+second+third)
# number = int(first+second+third)
# print(number)

# condi = True
# if 'AEIOUY' not in a:
#     print("Invalid")
# else:
#     for i in range(length - 1):
#         val = number[i] + number[i + 1]
#         if val%2 == 0:
#             condi = True
#         else:
#             condi = False

            
#     if condi:
#         print("valid")
#     else:
#         print("Invalid")

# a = "13X357-22"
# one = False
# two = False
# three = False
# four = False
# five = False
# six = False
# seven = False

# for i in range(len(a) - 1):
#     if i == 0:
#         sum = int(a[0])+int(a[i+1])
#         if sum%2 == 0:
#             one = True

#     if i == 2:
#         if "AEIOUY" not in a:
#             two = True

#     if i == 3:
#         sum = int(a[3])+int(a[4])
#         if sum%2 == 0:
#             three = True

#     if i == 4:  
#         sum = int(a[4])+int(a[5])
#         if sum%2 == 0:
#             four = True
#     if i == 6:
#         if a[i] == '-':
#             five = True
#     if i == 7:
#         sum = int(a[7])+int(a[8])
#         if sum%2 == 0:
#             six = True

# if one and two and three and four and five and six:
#     print("Valid")
# else:
#     print("Invalid")

# from collections import Counter

# # Sample list
# numbers = [1,1,2,2,4]

# # Count of every number in the list
# number_counts = Counter(numbers)
# c = (max(number_counts.values()))
# print(number_counts)
# print(number_counts[c])
# m = 0
# for i in enumerate(number_counts.values()):
#     if c == i[1]:
#         m+=1
#         print(i)
    
# print(m)



# if a[0] in '+-.':
#     f = float(a)
#     if f.__float__():
#         if a.count('.') == 1:
#             print(True)

# else:
#     print(False)
# n = 5
#fibonacci

# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

#pattern - 1 
# n = 5
# k = 1
# t = n
# for i in range(n):
#     while(k <= t):
#         print(k,end=" ")
#         k+=1
#     print()
#     t = t + n
    
# for i in range(5):
#     print(str(i+1)*(i+1))

#pattern - 2
# j = 0
# k = 0
# for i in range(5):
#     while j <= i:
#         print(k,end=' ')
#         j+=1
#         k +=1
#     print()
#     j = 0
#     k = i

#pattern-3
# j = 1
# k = 1
# for i in range(1,6):
    
#     while j <= i:
#         print(k,end=" ")
#         j+=1
#         k+=1
#     print()
#     k = j
#     j = 1

#pattern - 4

# n = 5
# j = 1
# for i in range(1,n):
#     while j <= i:
#         print(i-j+1,end=' ') #jugaad
#         j+=1
#     print()
#     j = 1

#Pattern - 5




# for j in range(3):
#     print(chr(65+j)*3)
    
#pattern - 6
# j = 0
# for i in range(3):
#     while j < 3:
#         print(chr(65+j),end=" ")
#         j+=1
#     print()
#     j = 0

#Pattern - 7

# n = 3
# j = 0
# k = 3
# for i in range(n):
#     while j < k:
#         print(chr(65+j),end=" ")
#         j+=1
#     print()
#     k+=n

#Pattern - 8

# n = 3
# j = 1
# for i in range(1,n+1):
#     while j <= n+1:
#         print(chr(65+i+j-2),end=' ')
#         j+=1
#     j = 1
#     print()

#Pattern - 9
# n = 14
# j = 0
# for i in range(n):
#     print(chr(65+i)*(i+1),end=' ')
#     print()

#Pattern - 10
# n = 5
# k = 0
# j = 0
# for i in range(n):
#     # print(" "*(i+1)+"* "*(n-i))
#     # print(" "*(n-i)+"* "*(i+1))
#     while j <= i:
#         print(chr(65+k),end=' ')
#         j+=1
#         k+=1
#     print() 
#     j = 0


#pattern - 11

# n = 4
# j = 1
# for i in range(1,n+1):
#     while j <= i:
#         print(chr(65+n-i+j-1),end=' ')
#         j += 1
#     j = 1
#     print()

#pattern - 12
# n = 5
# for i in range(1,n):
#     # print(" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1))
#     # print(' '*(n - i)+'*'*i)
#     # print('*'*(n - i))
#     print(' '*(i-1) + str(i)*(n - i))

#Pattern - 13


# l = "123456789"
# n = len(l)
# for i in range(len(l)):
#     if i == 0:
#         print(" "*(n - i) + l[0:i+1])
#     else:
#         # print(" "*(n - i) + l[0:i+1] + " "*(i) + l[0:i+1])
#         print(' '*(n - i) + l[0:i+1] + l[i - 1::-1])

# l = [1,0,4,3,0,2,1]
# cnt = 0
# for i in range(len(l)):
#     if l[i]:
#         temp = l[cnt]
#         l[cnt] = l[i]
#         l[i] = temp
#         # l[cnt] = l[i]
#         cnt += 1

# # while cnt < len(l):
# #     l[cnt] = 0
# #     cnt+=1

# print(l)


# s = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(s)):

# # print(s[0:len(s)])
#     if i == 0:
#         val = ''.join(str(i) for i in s)
#         print(val[len(s) - i::-1])
#     else:
#         print(val[len(s) - i - 1:: -1])
# print(s[len(s) - 2::-1])
# print(s[len(s) - 3::-1])
# print(s[len(s) - 4::-1])
# print(s[len(s) - 5::-1])

#Pattern - Hard
# n = 4
# m = n * 2
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if i == 1:
#             if j <= (m//2):
#                 print(j,end='')
#             else:
#                 print(m-j+1,end='')

#         else:
#             if j <= (m//2 - i + 1):
#                 print(j,end='')
#             elif j >= (m//2 + i):
#                 print(m-j+1,end='')
#             else:
#                 print('*',end='')
#     print()

#Bitwise operator
# print(~2)
# print(17>>1)

# print(17 >> 2)

# print(17 >> 3)
# cnt = 0
# n = 5
# while(n!=0):
    # if n&1 == 1:
    #     cnt += 1
    # n = n>>1
    # n = n&(n - 1)
    # cnt+=1

# print(cnt)
#101
#100
# Enter your code here. Read input from STDIN. Print output to STDOUT

#Decimal to Binary
# n = 5
# rev = 0
# i = 0
# tempn = n
# while n != 0:
#     bit = n & 1
#     rev = bit*pow(10,i) + rev
#     n = n >> 1
#     # print(bit,end='')
#     i+=1

# print(rev)
# i = 0
# ans = 0
# while(rev != 0):
#     bit = tempn%10
#     tempn = tempn // 10
#     if bit == 0:
#         ans = ans + pow(2,i)
#     i+=1
# print(ans)
#Binary to Decimal

# n = 10000
# ans = 0
# i= 0
# while n!=0:
#     bit = n%10
#     n = n // 10
#     if bit:
#         ans = ans + pow(2,i)
    
#     i+=1

# print(ans)


#Reverse a integer
# n = -123
# ans = 0
# i = 0

# n = abs(n)
# while n!=0:
#     bit = n%10
#     if bit == '-':
#         break
#     n = n // 10
#     # ans = bit*pow(10,i) + ans
#     ans = ans * 10 + bit
#     i+=1
# print(ans)

# a = -1534236469
# print(abs(a).bit_length())


# l = [1,2,3,4,5,6]
# for i in range(1,len(l)-1,2):
#     # a,b = b,a
#     l[i - 1],l[i] = l[i],l[i - 1]

# print(l)


# a = [1,1,2,2,2,4,1,2,1,4]

# s = {}

# for i in range(len(a)):
#     if a[i] in s:
#         s[a[i]] += 1
#     else:
#         s[a[i]] = 1

# print(s)
# ans = set(s.values())
# print(ans)

# a = [4,3,2,7,8,2,3,1]
# for i in range(len(a)):
#     val = abs(a[i])
#     val = val - 1
#     if a[val] > 0:
#         a[val] = -a[val]
#     else:
#         print(abs(a[val]))
    

#sort 1 and 0

# a = [1,0,0,0,0,0]
# l = len(a)
# j = 0
# i = 0
# while j < l:
#     if a[i] == 1 and a[j] == 0:
#         a[i],a[j] = a[j],a[i]
#         i+=1
#         j+=1

#     elif a[j] == 1:
#         j+=1
    
    
# print(a)
    
# sort 1 and 0 and 2
# a = [0,1,2,2,1,0,2,1]
#[1,2,2,0,0,2,2,1]
# a = [2,0,2,1,1,0]
# i = 0
# j = 0
# k = len(a)-1
# while j <= k:
#     if a[j] == 0:
#         a[i],a[j] = a[j],a[i]
#         i+=1
#         j+=1
#     elif a[j] == 2:
#         a[j],a[k] = a[k],a[j]
#         k-=1
#     elif a[i] == 1 and a[j] == 0:
#         a[i],a[j] = a[j],a[i]
#         i+=1
#         j+=1
    
#     elif a[j] == 1:
#         j+=1

# print(a)

# s = "i love programmming"
# ans=""
# for i in s.split():
#     ans+=i.capitalize()
#     ans+=" "

# print(ans)
#------------
# s = "Geeks"
# ans = []
# # print(s.center(7,'*'))
# for i in range(len(s)):
#     ans.append('.'*i + s[i:])
    
# ans = "".join(ans)
# print(ans)


#Binary Search(Left most Occurence)

a = [5,7,7,8,8,10]

#Below is Binary Search Code

# def binarySearch(arr, l, r, x):

#     # Check base case
#     if r >= l:

#         mid = int(l + (r - l)/2)

#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid

#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)
#         # Else the element can only be present in right subarray
#         else:
#             return binarySearch(arr, mid + 1, r, x)

#     else:
#         # Element is not present in the array
#         return -1
# print(binarySearch(a,0,len(a)-1,8))
