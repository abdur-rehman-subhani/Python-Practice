num=int(input("Enter the number: "))

match num:
    case 1:
        print("number is 1")
    case 0:
        print("number is 0")
   
    # case with if
    case _ if num!=100:
        print("number is not equal to 100")
        
     # default case
    case _ :
        print("number is in defaut case")
