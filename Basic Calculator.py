# num1=float(input("Enter 1st number: "))
# num2=float(input("Enter 2nd number: "))
# def sum(a,b):
#     return a+b
# def subtraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     return a/b
# def modulus(a,b):
#     return a%b
# if (num1==0 or num2==0 ):
#     print("\"Division or multiplication by zero is not allowed.\nEnter a non-zero number\"")
   
# else:
#     print("The sum of 1st and 2nd number is:", sum(num1,num2))
#     print("The subtraction of 1st and 2nd number is:", subtraction(num1,num2))
#     print("The multiplication of 1st and 2nd number is:", multiplication(num1,num2))
#     print("The division of 1st and 2nd number is:",division(num1,num2))
#     print("The modulus of 1st and 2nd number is:",modulus(num1,num2))

def sum(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
def multiplication(a,b):
    return a*b

num1=float(input("Enter First number: "))
operator=input("Enter the Operator (+,-,*,/): ")
num2=float(input("Enter Second number: "))
# for i in range:
match operator :
     case '+':
         print(f"The sum of {num1} and {num2} is: ",sum(num1,num2))
     case '-':
         print(f"The subtracion of {num1} and {num2} is: ",subtraction(num1,num2))
     case '*':
         print(f"The multiplication of {num1} and {num2} is: ",multiplication(num1,num2))
     case '/':
         print(f"The division of {num1} and {num2} is: ",division(num1,num2))

# calculation=input("Do you want another calculation (Yes/No)")
# if(calculation=='Yes'):
#     num1=float(input("Enter First number: "))
#     operator=input("Enter the Operator (+,-,*,/): ")
#     num2=float(input("Enter Second number: "))
# else:
#     print("Program ended successfullt..!")
