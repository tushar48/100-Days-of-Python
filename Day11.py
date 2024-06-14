#Exercise - 1

import time as t

time_string = t.strftime("%H:%M:%S",t.localtime())
print(time_string)

#Correct Answer

# time = 12


# while(True):
#     time_string = t.strftime("%H:%M:%S",t.localtime())
#     t.sleep(1)
#     actual_time = int(time_string[0:2])
#     # actual_time = 00
#     if(actual_time < time):
#         print("Good Morning")
#     else:
#         if actual_time >= time and actual_time <= 16:
#             print("Good Noon")
#         elif actual_time > 16 and actual_time <= 19:
#             print("Good Evening")
#         else:
#             print("Good Night")

