# We can check whether the element is present in the list or not 
colors=['Blue','Green','Yellow','Black']
print(type(colors))
if 'Yellow' in colors:
    print("Yes, Yellow is present in colors ")
else:
    print("No, Yellow is not present in colors ")


marks=[23,43,4,3,54]
print(marks)
if 43 in marks:
    print("Yes it is present ")

#Accessing the elemsts of list by its index
# Positive Indexing 
# print(marks[0]) 
# print(marks[1]) 
# print(marks[2]) 
# print(marks[3]) 
# print(marks[4]) 
# print(marks[5]) #It throws an error of index out of range 
# Negative Idexing 
print(marks[-1]) #Similar to positive indexing, negative indexing is also used to access items, 
print(marks[-2]) #but from the end of the list. The last item has index [-1], second last item has 
print(marks[-3]) #index [-2], third last item has index [-3] and so on.
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index
print(marks[:])
print(marks[0:-3])

# Example: printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax:
# List = [Expression(item) for item in iterable if Condition]
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
#Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)