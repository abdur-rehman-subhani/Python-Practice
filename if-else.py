# If-else example
age=int(input("Enter your age: "))
if(age>18):
    print("You can Drive...!")
else:
    print("You can't Drive...!")

# Example of elif
num=int(input("Enter the value of num:"))
if(num<0):
    print("The number is negative ")
elif(num==0):
    print("The number is zero")
else:
    print("The number is positive")

# Example of nested if-else
num=int(input("Enter the value of num:"))
if(num==0):
     print("The number is zero")
elif(num>0):
    if(num<=10):
        print("The number is between 1 and 10")
    elif(num>10 and num<=20):
        print("The number is between 10 and 20")
    else:
        print("The number is positive")
else:
    print("The number is negative")