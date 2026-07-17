# # 1. Default Arguments
# def Average(a=5,b=5):
#     print("The Average is: ", (a+b)/2)
# Average()
# #We can change the value of a or b by our own choice if no value is changed default values are used 
# Average(a=1)
# # 2. Keyword Arguments ...
# Average(b=1,a=9) #Here Order doesn't matter
# # 3. Required Arguments
# def Average(a,b,c=5):
#     print("The Average is: ",(a+b+c)/3)
# Average(2,4)
# 4. Keyword Arbitrary Arguments
# def average(*numbers):
#     print("The Type of numbers is:",type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#         print("The Average is:",sum/len(numbers))

# average(5,2,1,4,5,2)

# def name(**name):
#     print("The type of name is:",type(name))
#     print("Hello",name["fname"],name["mname"],name["lname"])
# name(fname="David",mname=["Jr."],lname=["Malan"])

# Return Arguments
def sum(a,b):
    return a+b
c=sum(2,3)
print(c)