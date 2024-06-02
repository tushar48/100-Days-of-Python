#Exercise - 1

import time as t

time_string = t.strftime("%H:%M:%S",t.localtime())
print(time_string)



time_hour = 12

# while(time_string):
    # t.sleep(1)
# hours = int(time_string[0:2])
hours = 18
if(hours >= time_hour):
    if(hours >= 12 and hours <= 16):
        print("Good Noon")
    elif (hours > 16 and hours <= 19):
        print("Good Evening")
    elif (hours > 19 and hours < 24 and time_string == "11:59:59"):
        print("Good Night")
else:
    print("Good Morning")
time_string = t.strftime("%H:%M:%S",t.localtime())

    