# # To perform operations on tuples first convert them into list then after operatios are performed , again convert them into tuple back
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# # Concatenation of tuples without converting them to lists 
# myCountries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# myCountries2 = ("Vietnam", "India", "China")
# southEastAsia = myCountries + myCountries2
# print(southEastAsia)

# Tuple Methods
number=(2,33,4,5,3,45,22,4,2,3)
print("The count of 3 is: ",number.count(3))
print("The index of first occurence of 4 is:",number.index(4))
# res = number.index(311) --> Throws an error'Index out of range'
res = number.index(3, 4, 8)
print(res)