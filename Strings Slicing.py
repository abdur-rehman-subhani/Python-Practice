# Strings Slicing 
fruit="Mango"
mangolen=len(fruit)
print(mangolen)
print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #incuding 1 but not 4
print(fruit[:5])
print(fruit[0:-3]) #Same
print(fruit[0:len(fruit)-3]) #Same
print(fruit[-1:len(fruit)-3]) 
print(fruit[-3:-1]) 

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
#Quick Quiz
nm="Harry"
print(nm[-4:-2])

#Strings are arrays and arrays are iterable. Thus we can loop through strings.
alphabets = "ABCDE"
for i in alphabets:
    print(i)