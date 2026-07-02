x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
# z=round(x+y) #This round function rounds off the value of decimal point to integer result 
# print(f"{z:,}")
#This :, in fString is used to place comma in 1000 like 1,000

# z=round(x/y, 2)
# Here passing 2 as second argument in round function. just rounds off the value of x/y upto 2 digits. Same thing can be done in fstring format just as i did below 
z=x/y
print(f"{z:.2f}")