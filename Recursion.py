# # Calling a function or using itself in it is called as recursion
# def factorial(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         return num *factorial(num-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# Fibonacci Series
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) #Recurssive Approach
    

    
print(fibonacci(6))
print(fibonacci(5))
print(fibonacci(4))
print(fibonacci(3))
print(fibonacci(2))
print(fibonacci(1))
print(fibonacci(0))





