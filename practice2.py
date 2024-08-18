#----------------------------------------------------
#Source-W3resource.com

#https://www.w3resource.com/python-exercises/python-basic-exercise-1.php

#Question-1

# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")

#Question-2
# import sys
# print(sys.version)

#Question-3

# import datetime

# print(datetime.datetime.now())


#Question-4

# import math
# r = float(input())

# print(math.pi * r ** 2)

#Question-5

# a,b = input().split()
# print(b,a)

#Question-6

# num = input()

# l = num.split(',')
# print(tuple(l))
# print(l)

#Question-7

# a = input()
# print(a.split('.')[1])


#Question-8

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[len(color_list) - 1])


#Question-9

# exam_st_date = (11, 12.1)

# print("The examination will start from : %i / %i / %i"%exam_st_date)
# print(" %i / %.2f "%exam_st_date)


#Question-10

# a = (input())

# b = a*2
# c = a*3

# print(int(a)+int(b)+int(c))


#Question-11

# print(abs.__doc__)

#Question-12

# import calendar

# print(calendar.month(2020,12))

#Question-13

# print("""This 
# is 
# multi line
# string""")

#Question-14

# import datetime

# f_date = datetime.date(2014,7,2)
# l_date = datetime.date(2114,7,11) 

# d = l_date - f_date

# print(d.days)

#Question-15
# import math
# print(4/3 * math.pi * 6**3)

#Question-16

# a = int(input())

# ans = a - 17

# if a > 17:
#     print(ans*2)
# else:
#     print(abs(ans))


#Question-17

# a = int(input())

# if abs(1000 - a) <= 100 or abs(2000-a) <= 100:
#     print("Near with Thousands")
# else:
#     print("Not at all")
    


#Question-18

# a,b,c = input().split()

# if a==b==c:
#     print((int(a)+int(b)+int(c))*3)

#Question-19

# a = input()

# if a[0:2] != 'ls':
#     print('ls '+a)

#Question-20

# a = input()
# print(a*3)


#Question-21

# print(int(input())&1 == 1)


#Question-22

# a = [1,4,6,7,4]
# print(a.count(int(input())))

#Question-23

# a = [1,5,8,3]
# if int(input()) in a:
#     print(True)
# else:
#     print(False)

#Question-24

# if input() in ['a','e','i','o','u']:
#     print(True)
# else:
#     print(False)


#Question-25

# a = input()
# copies = int(input())

# if copies < 2:
#     print(a)
# else:
#     print(a[0:copies]*copies)


#Question-26

# a = [2,3,6,5]

# for i in a:
#     print('@'*i)

#Question-27

# a = [1,5,12,2]

# ans = ''

# for i in a:
#     ans = ans + str(i)

# print(ans)

# s = ["this", "is", "a", "list"]

# print(" ".join(s)) # if it was string then it would be not joined 

# print(''.join(list(map(lambda a:str(a),a))))

# print("".join(str(i) for i in a ))

#Question-28

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for i in numbers:
#     if i == 237:
#         break
#     elif not (i&1):
#         print(i)

#Question-29

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1.difference(color_list_2))


#Question-30

# b = float(input())
# h = float(input())

# print(0.5*b*h)
    
#Question-31

# a = int(input())
# b = int(input())

# while(a%b != 0):
#     rem = a%b
#     a = b
#     b = rem

# print(math.gcd(a,b))
# import math
#Question-32

# a = int(input())
# b = int(input())
# big = max(a,b)
# while(True):
#     if((big%a) == 0 and (big%b) == 0):
#         break
#     big = big + 1
# print(big)

#Question-33

# a = []
# for i in range(3):
#     s = int(input())
#     if s not in a:
#         a.append(s)
#     else:
#         print(0)
#         break


# print(sum(a) if len(a) == 3 else "")

#Question-34

# a,b = input().split()
# s = int(a)+int(b)
# print(s if s > 15 and s < 20 else 20)

#Question-35

# a,b = input().split()
# a = int(a)
# b = int(b)
# if a == b or (a-b) == 5:
#     print(True)
# else:
#     print(False)

#Question-36

# a = 12
# b = 12.1
# if not isinstance(a,int) or not isinstance(b,int):
#     print(False)
# else:
#     print(a+b)

#Question-37

# amt = 10000
# inte = 3.5
# year = 7

# print(amt*(1+(inte/100))**year) # Future values

#Question-38

# import os.path

# print(os.path.isfile('fslag.txt'))

#Question-39

# from subprocess import call

# call(["ls","-l"])

#Question-40
# import os

# print("Current file name ",os.path.realpath(__file__)) #get real path 

#Question-41

# import multiprocessing

# cpu_count = multiprocessing.cpu_count()
# print(cpu_count)

#Question-42

# for i in range(0,10):
#     print(i,end="")


#Question-43



