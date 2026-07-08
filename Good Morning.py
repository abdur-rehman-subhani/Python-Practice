import time
timestamp=time.strftime("%H:%M:%S")
print("In Pakistan, Current time is:",timestamp)
timestamp=int(time.strftime('%H'))
# print(timestamp)
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(timestamp)
if(timestamp>6 and timestamp<12):
    print("Good morning Sir...!")
elif(timestamp>=12 and timestamp<5):
    print("Good Afternoon  Sir...!")
elif(timestamp>5 and timestamp<8):
    print("Good Evening Sir...!")
else:
    print("Good night Sir...!")