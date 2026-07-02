#if we want to use quotations marks in quotation marks
print("Hello, \"Friend\"")
#In python we can Literally use both Double and single quotes 
print('Hello, "Friend"')
#Sep and end parameters are in Print function's official documentation ..
#Sep is used as separater between two strings..Like we can add space 
#between strings if we want..End='\n' is for a new line.. End='' is for 
#keeping cursor on same line  without moving to next line 
name=input("What's your name ? ")
print("Hello," ,end='')
print(name)
print("Hello," ,sep='  ')
print(name)