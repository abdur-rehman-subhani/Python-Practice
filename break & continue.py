for i in range(0,10):
    if(i==6):
        break
    print("5 *",i+1,"=", 5*(i+1))
print("Exit the loop ")

j=3
for x in range(0,10):
    if(x==6):
        print('Skip the Iteration' )
        continue
    print(j,'*',x+1,'=', j*(x+1))

# Emulaion of do-while loop 
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
