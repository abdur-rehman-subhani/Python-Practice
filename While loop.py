# Prints the numbers till 10
i=0
while(i<=10):
    print(i)
    i=i+1

# Ask the user for input repetatively until gets number geater than 38
i=0
while(i<=38):
    i=int(input("Enter a number: "))
    print(i)

# Incrementing while loop
i=0
while(i<=5):
    print(i)
    i=i+1
# Decrementing while loop
i=5
while(i>0):
    print(i)
    i=i-1
# Loop with Else (If condition is not satisfied Else body will be executed)
i=-5
while(i>0):
    print(i)
    i=i-1
else:
    print("I am inside else")


'''
Syntax of do while loop 
do{
   Loop Body 
}while(condition);
 Emulate do-While loop (A Frequently asked question in python )
This can be achieved using Break and continue statements 
'''