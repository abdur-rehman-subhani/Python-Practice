def is_Prime(num):
    if (num%2!=0 and num%1==0):
        print("The entered number \"",num,"\" is prime number")
    else:
        print("The entered number \"",num,"\"is a composite number")


number=int(input("Enter a number: "))
is_Prime(int(number))
