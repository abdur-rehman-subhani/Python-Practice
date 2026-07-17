def print_gMean(a,b):
    gMean=(a*b)/(a+b)
    print("The Geametric Mean of",a,"And",b,"is:",gMean)

def find_Average(a,b):
    avg=(a+b)/2
    print("The Avera ge of",a,"and",b, "is", avg)

def is_Greater(a,b):
    if (a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)

# If I want to write function body on some other day when needed I can use the pass keyword 
def is_lesser(a,b):
    pass

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))
print_gMean(num1,num2)
find_Average(num1,num2)
is_Greater(num1,num2)

