# Single Line Strings --> We can use both single and double quotes in case of strings 
name="Harry"
Friend='David'
print(name)
print(Friend)
# Checking wether the element is present in the string or not 
if "Ha" in "Harry":
  print("Yes")

# Multi- Line Strings 
apple="""This is an apple .
An Apple a day,
Keeps a doctor away""" 
orange=''' This is an orange.
It is a Fruit. 
we should eat it. '''
print(apple)
print(orange)
# In Python, String is like an array of characers. we can access parts(Characters) of string by using its index which starts from 0
print(name[0]) 
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# We can print characters or parts of string through for loop
for character in apple:
    print(character)