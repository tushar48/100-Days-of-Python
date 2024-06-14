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


s = input()   


s = sorted(s, key = lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))
print(*s, sep="")

